import unittest
from src.split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_split_code_delimiter(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is text with a ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "code block")
    self.assertEqual(new_nodes[1].text_type, TextType.CODE)
    self.assertEqual(new_nodes[2].text, " word")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

  def test_split_bold_delimiter(self):
    node = TextNode("This is **bold text** example", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "bold text")
    self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
    self.assertEqual(new_nodes[2].text, " example")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

  def test_split_italic_delimiter(self):
    node = TextNode("This is _italic text_ example", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "italic text")
    self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
    self.assertEqual(new_nodes[2].text, " example")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

  def test_no_split_on_non_text_node(self):
    node = TextNode("This is a link", TextType.LINK, url="http://example.com")
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(len(new_nodes), 1)
    self.assertEqual(new_nodes[0], node)