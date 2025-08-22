from src.split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType

def text_to_textnode(text: str) -> list[TextNode]:
  node_list = [TextNode(text, TextType.TEXT)]
  node_list = split_nodes_delimiter(node_list, '`', TextType.CODE)
  node_list = split_nodes_delimiter(node_list, '**', TextType.BOLD)
  node_list = split_nodes_delimiter(node_list, '_', TextType.ITALIC)
  node_list = split_nodes_image(node_list)
  node_list = split_nodes_link(node_list)
  return node_list
