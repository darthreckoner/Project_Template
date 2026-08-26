# Domain and Intent Routing

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- Read the relevant sections of **`docs/VISION.md`**, **`docs/REQUIREMENTS.md`**, and
  **`docs/ARCHITECTURE.md`** when the task might affect accepted intent.
- Read **`docs/decisions/README.md`** before opening an ADR, then read only decisions relevant to
  the area being changed.
- Read an activated glossary only when the repository explicitly designates it as supporting domain
  knowledge; it is not a required parallel source of truth.

## File structure

This repository's canonical layout:

```
/
├── docs/VISION.md
├── docs/REQUIREMENTS.md
├── docs/ARCHITECTURE.md
├── docs/decisions/
│   ├── README.md
│   ├── proposed/
│   └── accepted/
└── src/
```


## Use canonical vocabulary

Use terminology defined by the relevant Vision, Requirements, Architecture, and accepted decisions.
When terminology is unresolved, propose a clarification in the most relevant existing artifact;
do not create a new glossary system solely to hold it.

## Flag ADR conflicts

If output contradicts an existing ADR, surface it explicitly rather than silently overriding it.
