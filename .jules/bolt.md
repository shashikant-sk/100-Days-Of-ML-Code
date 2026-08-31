## 2024-05-24 - Performance: HTML <img> tags in Markdown
**Learning:** This repository is heavily reliant on inline HTML `<img>` tags for displaying large infographics within its Markdown files. Since there are many images and no native application handling lazy loading, these embedded `<img>` tags create a performance bottleneck on page load by fetching all infographics simultaneously.
**Action:** When optimizing performance in Markdown-heavy repositories like this, look for embedded HTML `<img>` tags and add `loading="lazy"` attributes. This simple web optimization drastically improves initial load times by deferring the fetching of off-screen images.

## 2026-08-31 - Performance: Direct Image Serving
**Learning:** Using `github.com/.../blob/...` URLs in HTML `<img>` tags forces the browser to load the entire GitHub UI wrapper instead of the raw image data, which is a significant performance bottleneck.
**Action:** Always use `raw.githubusercontent.com/...` URLs for embedding GitHub-hosted images to serve the raw image data directly, bypassing the UI and drastically improving load times.
