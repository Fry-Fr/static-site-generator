import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode("div", None, None, {"class": "container"})
    node2 = HTMLNode("div", None, None, {"class": "container"})
    self.assertEqual(node, node2)
    
  def test_not_eq(self):
    node = HTMLNode("div", None, None, {"class": "container"})
    node2 = HTMLNode("span", None,None, {"class": "container"})
    self.assertNotEqual(node, node2)

  def test_props_is_none(self):
    node = HTMLNode("p")
    self.assertIsNone(node.props)
  
  def test_props_is_not_none(self):
    node = HTMLNode("a", None, None, {"href": "http://example.com"})
    self.assertIsNotNone(node.props)
  
  def test_to_html_not_implemented(self):
    node = HTMLNode("div")
    with self.assertRaises(NotImplementedError) as cm:
      node.to_html()
    self.assertEqual(str(cm.exception), "Error: to_html method must be implemented by subclasses")
