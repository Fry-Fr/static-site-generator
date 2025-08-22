import os
from src.generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generates pages from markdown files in the specified directory.

    Args:
        dir_path_content (str): The path to the directory containing markdown files.
        template_path (str): The path to the HTML template file.
        dest_dir_path (str): The destination directory where generated HTML files will be saved.
    """
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        
        if os.path.isdir(item_path):
            # Recursively process subdirectories
            dest_dir_path_subdir = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, dest_dir_path_subdir)
        elif item.endswith('.md'):
            # Generate HTML page from markdown file
            output_file = os.path.join(dest_dir_path, f"index.html")
            generate_page(item_path, template_path, output_file)