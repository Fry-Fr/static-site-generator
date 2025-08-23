import os
from src.extract_title import extract_title
from src.markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, destination_path, basepath="/"):
    print(f"Generating page from {from_path} to {destination_path} using template {template_path}")
    markdown_content = ""
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    template = ""
    with open(template_path, 'r') as f:
        template = f.read()
    title = extract_title(markdown_content)
    html_content = markdown_to_html_node(markdown_content).to_html()
    final_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content).replace('href="/"', f'href="{basepath}"').replace('src="/"', f'src="{basepath}"')

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    with open(destination_path, 'w') as f:
        f.write(final_content)