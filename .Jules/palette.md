## 2024-05-24 - Accessibility: HTML <img> tags in Markdown
**Learning:** This repository heavily uses inline HTML `<img>` tags within its Markdown files to center infographics, rather than using standard Markdown image syntax (`![alt](url)`). Many of these `<img>` tags lack `alt` attributes, making them inaccessible to screen readers.
**Action:** When working on accessibility in this repo, use scripts to automatically find and inject descriptive `alt` attributes into inline HTML `<img>` tags across Markdown files, as doing it manually is tedious and error-prone. Ensure temporary scripts used for such batch operations are deleted before committing.

## 2026-08-21 - Descriptive link text for screen readers
**Learning:** Avoid using generic link text like "here" (e.g., "click here" or "get it from here"). Screen readers often read links out of context, so the link text needs to clearly describe the destination.
**Action:** Always replace generic link text with descriptive alternatives (e.g., "[the dataset](url)" instead of "[here](url)") to maintain screen-reader accessibility standards.
