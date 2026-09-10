# GPT Image 2.5 Prompt Art Director

**English** | [简体中文](README.zh-CN.md)

Turn an image idea into a clear, detailed prompt for GPT Image 2.5.

This Codex skill helps you decide what the image should communicate, work through important visual choices, and write a complete prompt you can use in your image-generation workflow. It discusses the work in Chinese and writes the final prompt in English.

**It writes prompts. It does not generate images or spend image credits.**

## What you can use it for

- Develop a brief idea into a well-defined image concept.
- Improve an existing prompt without losing its important requirements.
- Give reference images clear roles, such as identity, clothing, composition, or style.
- Write instructions for local edits and follow-up revisions.
- Explore different visual directions before choosing one.
- Check whether a prompt contains conflicting, unnecessary, or hard-to-show details.

The skill covers people and fashion, products and food, architecture, nature, storytelling, graphic design, diagrams and interface previews, abstract art, surface patterns, and image series. It supports photography, painting, illustration, 3D, printmaking, collage, and mixed media.

It does not assume every image should be realistic, luxurious, or highly detailed. A simple abstract composition should stay simple when that serves the idea.

## How it works

For a clear request, the skill can write the prompt directly. For a complex or open-ended brief, it discusses the choices that would meaningfully change the result before drafting.

It checks the draft from two angles: whether it preserves your requirements, and whether the visual choices work together. It then validates the final text length.

You receive:

- A complete, copyable English prompt.
- A Chinese note with its verified character count, when local validation is available.
- Brief explanations or generation-setting suggestions when they are useful.
- A matching text file for prompts longer than 8,000 characters, or whenever you request one.

Each prompt is limited to **31,500 characters, including spaces and line breaks**. This is a limit set by this skill, not a claimed GPT Image 2.5 API limit. There is no minimum length, and the skill should not add repetition just to make a prompt longer.

## Install

1. Download this repository using **Code → Download ZIP**, then unzip it.
2. Rename the extracted folder to `gpt-image-2-5-prompt` if GitHub added a branch suffix such as `-main`.
3. Place the entire folder in your Codex skills directory: `~/.codex/skills/`, or `$CODEX_HOME/skills/` if you configured a custom location.
4. Keep all the included folders together. Copying only `SKILL.md` leaves out the guidance and validator it uses.

The final layout should look like this:

```text
~/.codex/skills/gpt-image-2-5-prompt/
├── SKILL.md
├── agents/
├── references/
├── scripts/
└── tests/
```

If you already have a version installed, keep a backup before replacing it. Python 3 is needed for exact character validation; the validator requires no additional Python packages.

## Start with a request

Invoke `$gpt-image-2-5-prompt`, then describe what you want. You can attach references or paste a prompt you already have.

For example:

```text
Use $gpt-image-2-5-prompt to develop a restrained product photograph
of a brushed-steel kettle. Keep the whole kettle visible, with no branding.
```

```text
Use $gpt-image-2-5-prompt to compare three visual directions for an
abstract exhibition poster before writing the final prompt.
```

```text
Use $gpt-image-2-5-prompt to improve the prompt below. Preserve the
character, pose, and clothing, and remove conflicting instructions.
```

You can write your request in Chinese. Prompt instructions are delivered in English, but any exact text you want inside the image is preserved in its original language.

## What to provide

Start with whatever you know. Helpful information includes the subject, intended use, preferred medium, composition, exact text, and anything that must stay unchanged.

For reference images, explain what each one should contribute. For edits, provide the original image and describe the change. You do not need to fill out a long questionnaire before getting started.

## Limits worth knowing

A better prompt improves the instructions; it cannot guarantee a perfect image. Text, identity, object geometry, and details outside an edit region still need checking in the generated result. Pixel-identical preservation requires a separate compositing workflow.

The skill tries to check the [official GPT Image 2.5 guide](https://developers.openai.com/api/docs/guides/image-prompting#gpt-image-2.5-guide) at the start of each new creative task. If it cannot access the page, it says so and uses its dated reference. If it cannot run the validator, it reports the count as unverified rather than inventing a number.

Initial validation covered the skill structure, 13 automated validator tests, and author-led example walkthroughs. It did not include image-generation quality testing.

This is an independently created skill, not an official OpenAI product.
