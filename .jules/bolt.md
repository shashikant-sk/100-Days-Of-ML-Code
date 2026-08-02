## 2026-08-02 - Lazy loading images in Markdown
**Learning:** This repository uses explicit HTML `<img>` tags in its Markdown files to embed large infographics. These images block initial rendering and consume large amounts of bandwidth on page load.
**Action:** Used `loading="lazy"` on all HTML image tags within Markdown files to defer loading off-screen images. When dealing with repos that are primarily documentation or curriculum, optimizing embedded assets is a key performance area.
