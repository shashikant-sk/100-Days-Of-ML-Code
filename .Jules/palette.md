## 2024-08-07 - Accessibility Anti-Pattern: HTML Images in Markdown without Alt Text
**Learning:** This repository extensively uses HTML `<img>` tags for displaying infographics in Markdown files instead of standard Markdown syntax (`![]()`). These HTML tags systematically lack the `alt` attribute, leading to a significant accessibility issue for screen readers.
**Action:** When working in repositories that rely heavily on HTML within Markdown for layout purposes (like centering), proactively check for and add missing `alt` attributes to ensure content remains accessible.
