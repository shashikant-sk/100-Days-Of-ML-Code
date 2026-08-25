## 2024-05-24 - Accessibility: HTML <img> tags in Markdown
**Learning:** This repository heavily uses inline HTML `<img>` tags within its Markdown files to center infographics, rather than using standard Markdown image syntax (`![alt](url)`). Many of these `<img>` tags lack `alt` attributes, making them inaccessible to screen readers.
**Action:** When working on accessibility in this repo, use scripts to automatically find and inject descriptive `alt` attributes into inline HTML `<img>` tags across Markdown files, as doing it manually is tedious and error-prone. Ensure temporary scripts used for such batch operations are deleted before committing.
## 2025-01-22 - Accessibility: Descriptive links
**Learning:** Generic link texts such as "[here](...)" were found across many markdown files in the repository. These provide no context to screen reader users who often navigate pages via a list of links.
**Action:** Automatically replace generic link texts with descriptive link text that indicates the target (e.g. `[the dataset](...)`, `[the code](...)`) to improve screen reader accessibility.
