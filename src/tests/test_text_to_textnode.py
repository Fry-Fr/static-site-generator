import unittest
from src.textnode import TextNode, TextType
from src.text_to_textnode import text_to_textnode

class TestTextToTextNode(unittest.TestCase):
    # Test converting text to TextNode
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnode(text)
        result_nodes = [
          TextNode("This is ", TextType.TEXT),
          TextNode("text", TextType.BOLD),
          TextNode(" with an ", TextType.TEXT),
          TextNode("italic", TextType.ITALIC),
          TextNode(" word and a ", TextType.TEXT),
          TextNode("code block", TextType.CODE),
          TextNode(" and an ", TextType.TEXT),
          TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
          TextNode(" and a ", TextType.TEXT),
          TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(len(nodes), len(result_nodes))
        self.assertListEqual(nodes, result_nodes)

    def test_empty_text(self):
        text = ""
        nodes = text_to_textnode(text)
        self.assertEqual(len(nodes), 0)
        self.assertListEqual(nodes, [])