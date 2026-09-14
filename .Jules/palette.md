## 2024-05-24 - Accessibility: HTML <img> tags in Markdown
**Learning:** This repository heavily uses inline HTML `<img>` tags within its Markdown files to center infographics, rather than using standard Markdown image syntax (`![alt](url)`). Many of these `<img>` tags lack `alt` attributes, making them inaccessible to screen readers.
**Action:** When working on accessibility in this repo, use scripts to automatically find and inject descriptive `alt` attributes into inline HTML `<img>` tags across Markdown files, as doing it manually is tedious and error-prone. Ensure temporary scripts used for such batch operations are deleted before committing.
## 2026-09-01 - Accessibility: Descriptive Links and Raw Image Paths
**Learning:** Using generic link text like "here" makes navigation difficult for screen readers. Using `blob` paths for GitHub images in HTML `<img>` tags returns HTML instead of raw image data.
**Action:** Ensure links use descriptive text rather than "here", and change `blob` to `raw.githubusercontent.com` for direct image embeds.
## 2024-09-13 - Accessibility: Descriptive Alt Text for Data Visualizations
**Learning:** Using generic terms like "data", "training", or "test" as `alt` text for machine learning visualizations (like DataFrames or decision boundary plots) fails to convey the structure or context of the visual information to screen reader users.
**Action:** When adding accessibility `alt` text to machine learning documentation, avoid generic terms. Use descriptive summaries that explain the context and structure of the visual results (e.g., 'Visualization of the training set results showing the decision boundary' or 'Screenshot of the dataset DataFrame showing User ID, Gender, Age, Estimated Salary, and Purchased status').
