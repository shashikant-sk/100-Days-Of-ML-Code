## 2024-05-24 - Accessibility: HTML <img> tags in Markdown
**Learning:** This repository heavily uses inline HTML `<img>` tags within its Markdown files to center infographics, rather than using standard Markdown image syntax (`![alt](url)`). Many of these `<img>` tags lack `alt` attributes, making them inaccessible to screen readers.
**Action:** When working on accessibility in this repo, use scripts to automatically find and inject descriptive `alt` attributes into inline HTML `<img>` tags across Markdown files, as doing it manually is tedious and error-prone. Ensure temporary scripts used for such batch operations are deleted before committing.
## 2026-08-24 - Improved screen-reader accessibility for links
**Learning:** The repository contained many generic links like "[here](...)". Screen reader users often navigate pages by tabbing through links. When links are simply labeled "here", they lack context, making navigation difficult.
**Action:** When adding or modifying links, always use descriptive link text (e.g., "[the dataset](...)") instead of generic terms like "here" to maintain screen-reader accessibility standards.
