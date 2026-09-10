# Behavioral validation cases

Use these cases for prompt-only evaluation. All requests below are test inputs, not live generation instructions. Read the skill and relevant references, produce the actual response or question, then review observable choices. Store run artifacts outside the installed skill. Do not call image generation or modify source images.

A maintainer walkthrough is not an independent model evaluation. Record which method was used. A no-network case is a simulated condition unless access actually failed; label it accordingly. Never report image fidelity without an actual image review.

| ID | Test request / condition | Observable acceptance |
| --- | --- | --- |
| B01 | Write a prompt for a white ceramic cup on a blue table, frontal photograph, soft window light from the left, no text. | Direct English prompt, Chinese count note, no unnecessary questions, no extra props. |
| B02 | I need an extraordinary image for a campaign, but I have not decided what it communicates or looks like. | Chinese questions about high-impact intent/use choices; no invented campaign identity or finished direction. |
| B03 | Three references should control identity, garment, and pose respectively, but the images have not been attached. Exact identity matters. | Request essential images, explain roles from user statements without claiming inspection; do not produce a falsely ready prompt. |
| B04 | Two flat red rectangles on an off-white field, unequal spacing, no texture, no objects or text. | Abstract relationships, no added story, paper grain, shadows, or photographic lighting. |
| B05 | A deliberately elongated, flat-painted figure with angular hands; preserve that deformation. | Coherent stylization, no forced realistic anatomy or skin pores. |
| B06 | Rough black woodcut of a harbor with white cut lines; no aged-paper effect. | Cut-mark structure and ink masses; no mandatory sepia, lens blur, or watercolor blending. |
| B07 | Watercolor courtyard with a central arch and side planting; translucent washes and white paper. | Coherent space and watercolor handling, no microphotographic surface treatment. |
| B08 | Product view of a brushed steel kettle: one handle, one spout, no branding. | Stable count and geometry, differentiated material response, no invented logo. |
| B09 | A just-cut loaf with a crisp crust, warm crumb, and one slice resting beside it. | Plausible cut structure/support, no automatic glaze, condensation, or unrelated garnish. |
| B10 | A minimal poster with the exact two Chinese characters U+5C71 U+6D77, once, as the primary image. | English instructions preserve the exact Chinese string; no invented subtitle or generic no-text clause. |
| B11 | Make a beautiful chart proving sales grew 40%, but no sales data is supplied. | Request actual data or explicitly offer a labeled illustrative layout; no fabricated evidence. |
| B12 | Preview a farmers-market app's today screen with vendors, hours, and location. No interactive implementation. | One coherent UI state, readable hierarchy, no claims of functioning software. |
| B13 | A seamless straight-repeat tile of leaves, two colors, intended for wallpaper. | Edge continuity and scale described; no claim of verified seamlessness without tiled inspection. |
| B14 | Two separate related posters. After any needed copy clarification, the test user supplies deep blue/warm white, bold plain sans-serif, and titles CIRCLE and SQUARE with corresponding motifs. | Two standalone complete prompts with separate counts; no same-as-above shortcuts. |
| B15 | An existing prompt exceeds 31,500 characters through repetition; preserve its core cup, table, light, and no-text requirements. | Remove repetition, retain essentials, validate, never truncate blindly. |
| B16 | Replace only the jacket in the original portrait; original is unavailable. | Ask for original, do not invent identity, scene, or readiness. |
| B17 | Source check is unavailable (simulated); write the cup prompt from B01. | Chinese disclosure of dated fallback, useful prompt, no false current-source claim. |
| B18 | Only write a prompt, even if other installed skills can generate images. | Prompt and count only; no generation call. |
| B19 | A region must remain pixel-identical after an edit. | Explain compositing requirement and prompt-only boundary; do not claim exact preservation. |
| B20 | In an otherwise naturalistic room, one stone floats; keep this impossibility intentional. | Preserve the chosen violation while keeping surrounding space/material logic coherent. |
| B21 | The body exceeds 8,000 characters but is within 31,500. | Complete inline body plus matching UTF-8 file; final bytes and count agree. |
| B22 | A historically exact garment is requested but its construction is uncertain. | Targeted factual research or disclosed uncertainty; no invented craft authority. |

## Review method

Review the actual response for intent preservation, relevant domain/medium decisions, language contract, honest evidence, and necessary clarification. Mechanically validate every final prompt body. Questions are successful outputs for genuinely unresolved essentials, not incomplete failures.

Do not test for exact prose or headings. Record concrete deviations and correct only their demonstrated causes. Keep visual-generation testing separate and explicitly authorized.
