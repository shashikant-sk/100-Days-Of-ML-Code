## 2024-05-18 - Replacing Raw `<img>` Tags with Proper `alt` Attributes

**Learning:** When creating Markdown documentation that leverages HTML `<img>` tags (e.g., for centered images), it is critical for screen reader accessibility to include descriptive `alt` attributes, as the standard Markdown image syntax (`![alt](url)`) is bypassed. In a large repository consisting primarily of visual infographics, lacking `alt` attributes creates a significant barrier for visually impaired users.
**Action:** Implemented a script to auto-generate and add descriptive `alt` attributes based on the filenames to all HTML `<img>` tags across the `.md` documentation files. In the future, always ensure that explicitly written HTML tags in Markdown maintain accessibility standards.
