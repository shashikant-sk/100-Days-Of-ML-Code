## 2024-06-25 - [Add alt tags to infographics in Markdown]
**Learning:** Found that this markdown repository relies heavily on raw HTML `<img>` tags for images rather than standard markdown `![]()` syntax, leading to widespread missing `alt` attributes.
**Action:** Created a targeted script to extract the context from markdown headers and automatically apply descriptive `alt` tags to these HTML images for improved screen reader accessibility. Ensure to look for `<img>` tags in markdown repos.
