import unittest
from src.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
      md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
      blocks = markdown_to_blocks(md)
      self.assertEqual(
          blocks,
          [
              "This is **bolded** paragraph",
              "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
              "- This is a list\n- with items",
          ],
      )

    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""""""), [])

    def test_single_paragraph(self):
        self.assertEqual(markdown_to_blocks("""
Hello, world!
"""), ["Hello, world!"])

    def test_multiple_paragraphs(self):
        markdown = """
First paragraph.

Second paragraph.

Third paragraph.
"""
        expected = ["First paragraph.", "Second paragraph.", "Third paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_leading_trailing_spaces(self):
        markdown = """
      Leading spaces.

      Trailing spaces.    
"""
        expected = ["Leading spaces.", "Trailing spaces."]
        self.assertEqual(markdown_to_blocks(markdown), expected)