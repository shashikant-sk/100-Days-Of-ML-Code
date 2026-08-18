import os
import re

def process_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find <img ...> tags
    # It handles multiline and different attributes
    img_pattern = re.compile(r'<img\s+([^>]+)>', re.IGNORECASE)

    def replace_img(match):
        attrs_str = match.group(1)

        # Check if alt is present
        has_alt = re.search(r'\balt\s*=\s*(["\'])(.*?)\1', attrs_str, re.IGNORECASE)
        # Check if loading is present
        has_loading = re.search(r'\bloading\s*=\s*(["\'])(.*?)\1', attrs_str, re.IGNORECASE)
        # Find src to generate alt if missing
        src_match = re.search(r'\bsrc\s*=\s*(["\'])(.*?)\1', attrs_str, re.IGNORECASE)

        new_attrs_str = attrs_str

        if not has_alt and src_match:
            src_url = src_match.group(2)
            # Extract filename from url
            filename = src_url.split('/')[-1]
            # Remove extension
            name_without_ext = os.path.splitext(filename)[0]
            # Replace %20 with space and hyphens/underscores with space
            import urllib.parse
            clean_name = urllib.parse.unquote(name_without_ext).replace('-', ' ').replace('_', ' ')
            new_attrs_str += f' alt="{clean_name}"'

        if not has_loading:
            new_attrs_str += ' loading="lazy"'

        return f'<img {new_attrs_str}>'

    new_content = img_pattern.sub(replace_img, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

def main():
    for root, dirs, files in os.walk('.'):
        # skip .git
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith('.md'):
                process_markdown_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
