## 2026-08-14 - Missing alt attributes on embedded HTML images
**Learning:** This repository extensively uses embedded HTML `<img>` tags within Markdown files to display infographics, but consistently omits the `alt` attribute. This creates a significant accessibility barrier for screen reader users, who receive no context for these educational images.
**Action:** Always add descriptive `alt` text when modifying or adding `<img>` tags in this repository. Use the surrounding context (e.g., preceding headings) to craft meaningful descriptions.
