## 2024-05-24 - Accessibility: HTML <img> tags in Markdown
**Learning:** This repository heavily uses inline HTML `<img>` tags within its Markdown files to center infographics, rather than using standard Markdown image syntax (`![alt](url)`). Many of these `<img>` tags lack `alt` attributes, making them inaccessible to screen readers.
**Action:** When working on accessibility in this repo, use scripts to automatically find and inject descriptive `alt` attributes into inline HTML `<img>` tags across Markdown files, as doing it manually is tedious and error-prone. Ensure temporary scripts used for such batch operations are deleted before committing.
## 2024-05-24 - Accessibility: Descriptive Link Texts
**Learning:** The Markdown files in this repository previously used generic link text like "[here](URL)", which is completely inaccessible for screen-reader users, as they are given no context when reading out links.
**Action:** Always replace "here" with a descriptive context word, such as "dataset", "code", or "playlist", e.g., `Get the [dataset](...)` or `Check the [code](...)`.
