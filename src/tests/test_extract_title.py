import unittest
from src.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
  def test_extract_title(self):
    self.assertEqual(extract_title("# My Title\nSome content."), "My Title")
    self.assertEqual(extract_title("   # Another Title   \nMore content."), "Another Title")
    self.assertEqual(extract_title("\n# Leading Newline\nContent."), "Leading Newline")
    self.assertEqual(extract_title("   \n   # Indented Title\nContent."), "Indented Title")
    self.assertEqual(extract_title("# Title with # in it #\nContent."), "Title with # in it #")
    self.assertEqual(extract_title("#    Title with Extra Spaces    \nContent."), "Title with Extra Spaces")

  def test_no_title(self):
    with self.assertRaises(ValueError) as context:
      extract_title("No title here.\nJust content.")
    self.assertEqual(str(context.exception), "No valid title found")
    with self.assertRaises(ValueError) as context:
      extract_title("## Subtitle\nContent.")
    self.assertEqual(str(context.exception), "No valid title found")
    with self.assertRaises(ValueError) as context:
      extract_title("### Another Subtitle\nContent.")
    self.assertEqual(str(context.exception), "No valid title found")
    with self.assertRaises(ValueError) as context:
      extract_title("   \n   \n   \n")
    self.assertEqual(str(context.exception), "No valid title found")