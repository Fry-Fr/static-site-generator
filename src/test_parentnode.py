import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )
  def test_to_html_with_multiple_children(self):
    node = ParentNode(
      "p",
      [
          LeafNode("b", "Bold text"),
          LeafNode(None, "Normal text"),
          LeafNode("i", "italic text"),
          LeafNode(None, "Normal text"),
      ],
  )
    self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

  def test_to_html_no_tag_raises_error(self):
    node = ParentNode("", [LeafNode("span", "child")])
    with self.assertRaises(ValueError) as context:
      node.to_html()
    self.assertEqual(str(context.exception), "Error: ParentNode must have a tag to convert to HTML")

  def test_to_html_no_children_raises_error(self):
    node = ParentNode("div", [])
    with self.assertRaises(ValueError) as context:
      node.to_html()
    self.assertEqual(str(context.exception), "Error: ParentNode must have children to convert to HTML")
