import re

def extract_title(markdown_text):
    match = re.search(r'^[ \t]*#\s+(.+)', markdown_text, re.MULTILINE)
    if match:
        h1_header = match.group(1)
        return h1_header.strip()
    else:
        raise Exception("No H1 header found.")
