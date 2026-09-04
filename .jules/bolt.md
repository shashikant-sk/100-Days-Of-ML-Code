## 2024-05-24 - Performance: HTML <img> tags in Markdown
**Learning:** This repository is heavily reliant on inline HTML `<img>` tags for displaying large infographics within its Markdown files. Since there are many images and no native application handling lazy loading, these embedded `<img>` tags create a performance bottleneck on page load by fetching all infographics simultaneously.
**Action:** When optimizing performance in Markdown-heavy repositories like this, look for embedded HTML `<img>` tags and add `loading="lazy"` attributes. This simple web optimization drastically improves initial load times by deferring the fetching of off-screen images.

## 2026-09-01 - Performance: Raw Image URLs in Markdown
**Learning:** Using `github.com/.../blob/...` URLs in HTML `<img>` tags serves a heavier page wrapper, whereas `raw.githubusercontent.com/...` serves the image bytes directly, significantly reducing overhead and improving load time.
**Action:** Always replace `github.com/.../blob/...` with `raw.githubusercontent.com/...` in `<img>` tag `src` attributes to optimize image loading performance.

## 2026-09-04 - Performance: Add decoding="async" to embedded images
**Learning:** When adding web performance optimizations to embedded HTML <img> tags in Markdown files (especially for large infographics), use `decoding="async"` alongside `loading="lazy"` to prevent the main thread from blocking during image decoding and to improve scrolling responsiveness.
**Action:** Ensure both `loading="lazy"` and `decoding="async"` are present on inline <img> tags to maximize rendering performance.
