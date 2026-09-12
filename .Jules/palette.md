## 2024-05-24 - Accessibility: HTML <img> tags in Markdown
**Learning:** This repository heavily uses inline HTML `<img>` tags within its Markdown files to center infographics, rather than using standard Markdown image syntax (`![alt](url)`). Many of these `<img>` tags lack `alt` attributes, making them inaccessible to screen readers.
**Action:** When working on accessibility in this repo, use scripts to automatically find and inject descriptive `alt` attributes into inline HTML `<img>` tags across Markdown files, as doing it manually is tedious and error-prone. Ensure temporary scripts used for such batch operations are deleted before committing.
## 2026-09-01 - Accessibility: Descriptive Links and Raw Image Paths
**Learning:** Using generic link text like "here" makes navigation difficult for screen readers. Using `blob` paths for GitHub images in HTML `<img>` tags returns HTML instead of raw image data.
**Action:** Ensure links use descriptive text rather than "here", and change `blob` to `raw.githubusercontent.com` for direct image embeds.
## 2026-09-12 - Accessibility: Meaningful alt text for data visualization images
**Learning:** In machine learning documentation and repositories, images are frequently used to showcase datasets and visual results (e.g., decision boundaries, confusion matrices). Providing generic alt text like "data", "training", or "test" fails to communicate the context and structure of these visuals to users relying on screen readers.
**Action:** When working on such repositories, always replace vague alt text with descriptive summaries (e.g., "Dataset snapshot showing user ID, gender, age, estimated salary, and purchased status" instead of "data").
