from src.recursive_copy import recursive_copy
from src.generate_pages_recursive import generate_pages_recursive

def main():
  recursive_copy("static", "public")
  generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
  main()
