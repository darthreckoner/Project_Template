# Domain and Intent Routing

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- Read the relevant sections of **`docs/VISION.md`**, **`docs/REQUIREMENTS.md`**, and
  **`docs/ARCHITECTURE.md`** when the task might affect accepted intent.
- Read **`docs/decisions/README.md`** before opening an ADR, then read only decisions relevant to
  the area being changed.
- Read **`CONTEXT.md`** or another glossary only if this repository activates one; it is not a
  required parallel source of truth.

If any of these files don't exist, proceed silently. Don't flag their absence or suggest creating them upfront. The domain-modeling skill creates them lazily when terms or decisions get resolved.

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


## Use the glossary's vocabulary

When output names a domain concept, use the terminology defined by the relevant requirements,
architecture, and accepted decisions. If an activated glossary exists, use it as supporting domain
knowledge rather than a competing authority.

## Flag ADR conflicts

If output contradicts an existing ADR, surface it explicitly rather than silently overriding it.
