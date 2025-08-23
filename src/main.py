import sys
from src.recursive_copy import recursive_copy
from src.generate_pages_recursive import generate_pages_recursive

basepath = "/"
destination_dir = "public"
if len(sys.argv) > 1:
  basepath = sys.argv[1]
if len(sys.argv) > 2:
  destination_dir = sys.argv[2]

def main():
  recursive_copy("static", destination_dir)
  generate_pages_recursive("content", "template.html", destination_dir, basepath)

if __name__ == "__main__":
  main()
