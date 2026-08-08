## 2024-03-24 - Markdown Static Site Performance
**Learning:** This repo is entirely Markdown files acting as a static site (via Jekyll). When rendering these files on GitHub or a static site generator, loading numerous high-res infographics (like in the 100-Days-Of-ML-Code README) eagerly blocks initial load and wastes bandwidth.
**Action:** Always consider `loading="lazy"` on heavy `<img>` tags inside Markdown files, especially for long READMEs containing multiple images below the fold.
