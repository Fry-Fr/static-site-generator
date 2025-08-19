import unittest
from textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodesDelimiter(unittest.TestCase):
  # Test splitting code with given delimiter
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

  # Test splitting link and image nodes
  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

  def test_split_image_node(self):
    node = TextNode("Here is an image ![alt text](http://image.url) in text", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "Here is an image ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "alt text")
    self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
    self.assertEqual(new_nodes[1].url, "http://image.url")
    self.assertEqual(new_nodes[2].text, " in text")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

  def test_split_link_node(self):
    node = TextNode("Here is a link [link text](http://link.url) in text", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "Here is a link ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "link text")
    self.assertEqual(new_nodes[1].text_type, TextType.LINK)
    self.assertEqual(new_nodes[1].url, "http://link.url")
    self.assertEqual(new_nodes[2].text, " in text")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
  
  def test_no_split_image_on_non_text_node(self):
    node = TextNode("This is a code block", TextType.CODE)
    new_nodes = split_nodes_image([node])
    self.assertEqual(len(new_nodes), 1)
    self.assertEqual(new_nodes[0], node)

  def test_no_split_link_on_non_text_node(self):
    node = TextNode("This is bold text", TextType.BOLD)
    new_nodes = split_nodes_link([node])
    self.assertEqual(len(new_nodes), 1)
    self.assertEqual(new_nodes[0], node)
