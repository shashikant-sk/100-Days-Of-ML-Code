## 2024-05-24 - Performance: HTML <img> tags in Markdown
**Learning:** This repository is heavily reliant on inline HTML `<img>` tags for displaying large infographics within its Markdown files. Since there are many images and no native application handling lazy loading, these embedded `<img>` tags create a performance bottleneck on page load by fetching all infographics simultaneously.
**Action:** When optimizing performance in Markdown-heavy repositories like this, look for embedded HTML `<img>` tags and add `loading="lazy"` attributes. This simple web optimization drastically improves initial load times by deferring the fetching of off-screen images.

## 2026-08-30 - Performance: Raw Image URLs
**Learning:** Using `github.com/.../blob/...` URLs in `<img>` tags fetches an HTML page wrapper rather than the raw image data, which introduces unnecessary latency. Using `raw.githubusercontent.com/...` bypasses this overhead and serves the image directly.
**Action:** Always replace `github.com/user/repo/blob/branch/path` with `raw.githubusercontent.com/user/repo/branch/path` in `<img>` `src` attributes for faster direct asset delivery.
