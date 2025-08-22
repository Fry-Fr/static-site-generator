def extract_title(markdown_text: str) -> str:
    lines = markdown_text.splitlines(keepends=False)
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('# '):
            title = stripped_line.lstrip('# ').strip()
            return title
    raise ValueError("No valid title found")
