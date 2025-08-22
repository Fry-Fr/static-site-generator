from src.recursive_copy import recursive_copy
from src.generate_page import generate_page

def main():
  recursive_copy("static", "public")
  generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
  main()
