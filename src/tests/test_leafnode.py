import unittest
from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
  
  def test_leaf_to_html_div_with_props(self):
    node = LeafNode("div", "Content", {"class": "container", "id": "main"})
    self.assertEqual(node.to_html(), '<div class="container" id="main">Content</div>')

  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Just text")
    self.assertEqual(node.to_html(), "Just text")

  def test_leaf_to_html_empty_value_raises(self):
    node = LeafNode("span", None) # type: ignore
    with self.assertRaises(ValueError) as context:
      node.to_html()
    self.assertEqual(str(context.exception), "Error: LeafNode must have a non-empty value to convert to HTML")
