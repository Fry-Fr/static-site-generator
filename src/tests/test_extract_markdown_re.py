import unittest
from src.extract_markdown_re import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownRe(unittest.TestCase):
  # Tests for extract_markdown_images function
  def test_extract_single_image(self):
    text = "Here is an image: ![Alt text](http://example.com/image.png)"
    images = extract_markdown_images(text)
    self.assertEqual(len(images), 1)
    self.assertEqual(images[0], ("Alt text", "http://example.com/image.png"))

  def test_extract_multiple_images(self):
    text = "Images: ![First](http://example.com/first.png) and ![Second](http://example.com/second.jpg)"
    images = extract_markdown_images(text)
    self.assertEqual(len(images), 2)
    self.assertEqual(images[0], ("First", "http://example.com/first.png"))
    self.assertEqual(images[1], ("Second", "http://example.com/second.jpg"))

  def test_no_images(self):
    text = "This text has no images."
    images = extract_markdown_images(text)
    self.assertEqual(len(images), 0)

  def test_image_with_empty_alt_text(self):
    text = "Image with empty alt text: ![](http://example.com/emptyalt.png)"
    images = extract_markdown_images(text)
    self.assertEqual(len(images), 1)
    self.assertEqual(images[0], ("", "http://example.com/emptyalt.png"))

  def test_image_with_special_characters_in_url(self):
    text = "Special chars: ![Special](http://example.com/image%20with%20spaces.png)"
    images = extract_markdown_images(text)
    self.assertEqual(len(images), 1)
    self.assertEqual(images[0], ("Special", "http://example.com/image%20with%20spaces.png"))

  # Test for extract_markdown_links function
  def test_extract_single_link(self):
    text = "Here is a link: [Example](http://example.com)"
    links = extract_markdown_links(text)
    self.assertEqual(len(links), 1)
    self.assertEqual(links[0], ("Example", "http://example.com"))

  def test_extract_multiple_links(self):
    text = "Links: [First](http://example.com/first) and [Second](http://example.com/second)"
    links = extract_markdown_links(text)
    self.assertEqual(len(links), 2)
    self.assertEqual(links[0], ("First", "http://example.com/first"))
    self.assertEqual(links[1], ("Second", "http://example.com/second"))
  
  def test_no_links(self):
    text = "This text has no links."
    links = extract_markdown_links(text)
    self.assertEqual(len(links), 0)

  def test_link_with_special_characters_in_url(self):
    text = "Special chars: [Special](http://example.com/page?arg=value&other=üñîçødé)"
    links = extract_markdown_links(text)
    self.assertEqual(len(links), 1)
    self.assertEqual(links[0], ("Special", "http://example.com/page?arg=value&other=üñîçødé"))
