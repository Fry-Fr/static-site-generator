import re

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
  pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  return re.findall(pattern, text)

import re

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
