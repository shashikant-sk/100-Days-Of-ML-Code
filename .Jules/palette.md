## 2024-05-18 - Missing Alt Attributes in Markdown Images
**Learning:** In markdown repositories that heavily rely on HTML `<img>` tags (e.g. to allow image centering or resizing), these tags frequently lack `alt` attributes, making the images inaccessible to screen readers. Standard markdown images (`![alt](src)`) enforce thinking about alt text, whereas HTML tags do not.
**Action:** When working with repositories that mix HTML and Markdown for formatting purposes, explicitly check for and add missing `alt` attributes to all `<img>` tags.
