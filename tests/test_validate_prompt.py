"""Boundary and serialization tests; no image-generation calls."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_prompt.py"
SPEC = importlib.util.spec_from_file_location("validate_prompt", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PromptValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def check_body(self, text):
        path = self.root / "body.txt"
        raw = text.encode("utf-8")
        path.write_bytes(raw)
        result = MODULE.validate_file(path)
        self.assertEqual(path.read_bytes(), raw, "Validation must be read-only")
        self.assertEqual(result["characters"], len(text))
        return result

    def codes(self, text):
        return {i["code"] for i in self.check_body(text)["issues"]}

    def test_limit_boundaries(self):
        for count in (31499, 31500, 31501):
            with self.subTest(count=count):
                result = self.check_body("a" * count)
                self.assertEqual(result["valid"], count <= 31500)
                self.assertEqual(result["over_limit"], count > 31500)

    def test_spaces_and_lf_count(self):
        self.assertTrue(self.check_body("A B\n\nC D")["valid"])

    def test_intra_paragraph_line_breaks(self):
        self.assertTrue(self.check_body("Copy:\nFirst line\nSecond line")["valid"])

    def test_unicode_code_points_not_graphemes_or_bytes(self):
        text = 'Render "\u5c71\u6d77" with \U0001f30a and e\u0301.'
        result = self.check_body(text)
        self.assertTrue(result["valid"])
        self.assertNotEqual(len(text), len(text.encode("utf-8")))
        self.assertEqual(len("e\u0301"), 2)
        self.assertEqual(len("\U0001f30a"), 1)

    def test_crlf_not_normalized(self):
        self.assertIn("non_lf_newline", self.codes("A\r\n\r\nB"))

    def test_outer_whitespace(self):
        for text in ("\nA", "A\n", " A", "A ", "\tA"):
            with self.subTest(text=text):
                self.assertIn("outer_whitespace", self.codes(text))

    def test_blank_lines(self):
        self.assertIn("extra_blank_lines", self.codes("A\n\n\nB"))
        self.assertIn("whitespace_blank_line", self.codes("A\n \nB"))
        self.assertIn("whitespace_blank_line", self.codes("A\n\t\nB"))

    def test_empty(self):
        for text in ("", " \n\t"):
            with self.subTest(text=text):
                self.assertIn("empty_body", self.codes(text))

    def test_invalid_utf8(self):
        path = self.root / "invalid.txt"
        path.write_bytes(b"\xff")
        result = MODULE.validate_file(path)
        self.assertIsNone(result["characters"])
        self.assertIsNone(result["over_limit"])
        self.assertEqual(result["issues"][0]["code"], "invalid_utf8")
        self.assertEqual(path.read_bytes(), b"\xff")

    def test_bom_and_controls(self):
        self.assertIn("bom", self.codes("\ufeffText"))
        self.assertIn("control_character", self.codes("A\x00B"))
        self.assertIn("non_lf_separator", self.codes("A\u2028B"))

    def test_read_error(self):
        result = MODULE.validate_file(self.root / "missing.txt")
        self.assertFalse(result["valid"])
        self.assertEqual(result["issues"][0]["code"], "read_error")

    def test_cli_multiple_files_and_exit(self):
        good = self.root / "good.txt"
        bad = self.root / "bad.txt"
        good.write_bytes(b"Valid prompt")
        bad.write_bytes(b"a" * 31501)
        run = subprocess.run([sys.executable, str(SCRIPT), "--json", str(good), str(bad)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 1)
        report = json.loads(run.stdout)
        self.assertFalse(report["valid"])
        self.assertEqual([r["characters"] for r in report["results"]], [12, 31501])
        good_run = subprocess.run([sys.executable, str(SCRIPT), str(good)], capture_output=True, text=True)
        self.assertEqual(good_run.returncode, 0)
        self.assertIn("PASS", good_run.stdout)

    def test_serialized_delivery_identity(self):
        body = 'Create a poster.\n\nRender "\u5c71\u6d77" exactly once.'
        scratch = self.root / "scratch.txt"
        delivered = self.root / "delivered.txt"
        scratch.write_bytes(body.encode("utf-8"))
        delivered.write_bytes(scratch.read_bytes())
        self.assertEqual(delivered.read_bytes().decode("utf-8"), body)
        self.assertEqual(MODULE.validate_file(delivered)["characters"], len(body))
        self.assertTrue(MODULE.validate_file(delivered)["valid"])


if __name__ == "__main__":
    unittest.main()
