## 2024-05-18 - Markdown Image Accessibility
**Learning:** Found that this repository relies heavily on raw HTML `<img>` tags embedded in Markdown files for displaying infographics. Many of these tags initially lacked descriptive `alt` attributes, making them inaccessible to screen readers.
**Action:** Always check `README.md` and other documentation files for raw HTML tags that might missing critical accessibility attributes. Added a note to ensure any utility scripts used for such updates are cleaned up before committing to maintain a clean history.
