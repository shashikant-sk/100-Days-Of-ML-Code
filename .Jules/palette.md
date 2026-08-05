## 2026-08-05 - HTML Image Tags in Markdown
**Learning:** This repository heavily uses raw HTML `<img>` tags inside Markdown files (e.g., to allow alignment), rather than standard Markdown syntax. This pattern masks missing `alt` text from standard markdown linting.
**Action:** When auditing Markdown files in this repo for accessibility, always grep for raw `<img` tags to ensure `alt` attributes are present.
