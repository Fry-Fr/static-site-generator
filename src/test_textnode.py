import unittest
from textnode import TextNode, TextType
class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
    
	def test_not_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.ITALIC)
		self.assertNotEqual(node, node2)

	def test_link_url_none(self):
		node = TextNode("This is a link", TextType.LINK)
		self.assertIsNone(node.url)
	
	def test_link_url_is_not_none(self):
		node = TextNode("This is a link", TextType.LINK, url="http://example.com")
		self.assertIsNotNone(node.url)
	
	def test_url_is_not_none(self):
		node = TextNode("This is an image", TextType.IMAGE, url="http://example.com/image.png")
		self.assertIsNotNone(node.url)

	def test_url_raises_exception(self):
		# Test that ValueError is raised when url is empty for IMAGE type
		with self.assertRaises(ValueError) as cm_1:
			TextNode("This is an image", TextType.IMAGE, url="")
		self.assertEqual(str(cm_1.exception), "Error: url must be provided for text_type IMAGE")
		# Test that ValueError is raised when url is None for IMAGE type
		with self.assertRaises(ValueError) as cm_2:
			TextNode("This is an image", TextType.IMAGE)
		self.assertEqual(str(cm_2.exception), "Error: url must be provided for text_type IMAGE")



if __name__ == "__main__":
    unittest.main()
