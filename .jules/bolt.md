## 2024-05-24 - Performance: HTML <img> tags in Markdown
**Learning:** This repository is heavily reliant on inline HTML `<img>` tags for displaying large infographics within its Markdown files. Since there are many images and no native application handling lazy loading, these embedded `<img>` tags create a performance bottleneck on page load by fetching all infographics simultaneously.
**Action:** When optimizing performance in Markdown-heavy repositories like this, look for embedded HTML `<img>` tags and add `loading="lazy"` attributes. This simple web optimization drastically improves initial load times by deferring the fetching of off-screen images.

## 2026-09-01 - Performance: Raw Image URLs in Markdown
**Learning:** Using `github.com/.../blob/...` URLs in HTML `<img>` tags serves a heavier page wrapper, whereas `raw.githubusercontent.com/...` serves the image bytes directly, significantly reducing overhead and improving load time.
**Action:** Always replace `github.com/.../blob/...` with `raw.githubusercontent.com/...` in `<img>` tag `src` attributes to optimize image loading performance.

## 2026-09-05 - Performance: Asynchronous Image Decoding
**Learning:** Large infographics embedded in Markdown using HTML `<img>` tags can block the main thread during image decoding, leading to poor scrolling responsiveness, even when lazy loaded.
**Action:** Add `decoding="async"` alongside `loading="lazy"` in `<img>` tags to allow the browser to decode these large images asynchronously, preventing UI jank and improving overall page performance.
