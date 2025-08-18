from enum import Enum
from textnode import TextNode, TextType

class SplitType(Enum):
  CODE = '`'
  BOLD = '**'
  ITALIC = '_'

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
  if delimiter not in [e.value for e in SplitType]:
    raise ValueError(f"Error: delimiter '{delimiter}' is not a valid SplitType value.")

  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    split_value = node.text.split(delimiter)
    new_nodes.append(TextNode(split_value[0], TextType.TEXT))
    match text_type:
      case TextType.CODE:
        new_nodes.append(TextNode(split_value[1], TextType.CODE))
      case TextType.BOLD:
        new_nodes.append(TextNode(split_value[1], TextType.BOLD))
      case TextType.ITALIC:
        new_nodes.append(TextNode(split_value[1], TextType.ITALIC))
    new_nodes.append(TextNode(split_value[2], TextType.TEXT))
  return new_nodes
