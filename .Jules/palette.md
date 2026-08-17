## 2024-05-18 - Adding Alt Text to Embedded Images
**Learning:** This repository heavily relies on raw HTML `<img>` tags embedded in Markdown instead of standard Markdown image syntax (`![alt](url)`). Many of these were missing `alt` attributes, making the educational infographics and data visualizations inaccessible to screen readers.
**Action:** When working on accessibility in this codebase, prioritize checking for embedded HTML tags and writing scripts to infer context (like day number or chart type) from the image URL to generate meaningful `alt` text.
