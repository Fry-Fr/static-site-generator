from enum import Enum
from src.textnode import TextNode, TextType
from src.extract_markdown_re import extract_markdown_images, extract_markdown_links

class SplitType(Enum):
  CODE = '`'
  BOLD = '**'
  ITALIC = '_'

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
  if delimiter not in [e.value for e in SplitType]:
    raise ValueError(f"Error: delimiter '{delimiter}' is not a valid SplitType value.")

  new_nodes = []
  for node in old_nodes:
    if node.text == '':
      continue
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    text = node.text.replace(delimiter, '|', 2)
    split_value = text.split('|')
    if len(split_value) < 2:
      new_nodes.append(node)
      continue
    if split_value[0] != '':
      new_nodes.append(TextNode(split_value[0], TextType.TEXT))
    match text_type:
      case TextType.CODE:
        new_nodes.append(TextNode(split_value[1], TextType.CODE))
      case TextType.BOLD:
        new_nodes.append(TextNode(split_value[1], TextType.BOLD))
      case TextType.ITALIC:
        new_nodes.append(TextNode(split_value[1], TextType.ITALIC))
    if len(split_value) > 2 and split_value[2] != '':
      new_nodes.append(TextNode(split_value[2], TextType.TEXT))
      return split_nodes_delimiter(new_nodes, delimiter, text_type)
  return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    images = extract_markdown_images(node.text)
    if not images:
      new_nodes.append(node)
      continue
    original_text = node.text
    while original_text:
      alt_text, url = images.pop(0)
      sections = original_text.split(f"![{alt_text}]({url})", 1)
      new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
      if len(sections) > 1 and len(images) > 0:
        original_text = sections[1]
      elif len(sections) > 1 and not images:
        if sections[1]:
          new_nodes.append(TextNode(sections[1], TextType.TEXT))
        original_text = ''
      else:
        original_text = ''
  return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    links = extract_markdown_links(node.text)
    if not links:
      new_nodes.append(node)
      continue
    original_text = node.text
    while original_text:
      text, url = links.pop(0)
      sections = original_text.split(f"[{text}]({url})", 1)
      new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append(TextNode(text, TextType.LINK, url))
      if len(sections) > 1 and len(links) > 0:
        original_text = sections[1]
      elif len(sections) > 1 and not links:
        if sections[1]:
          new_nodes.append(TextNode(sections[1], TextType.TEXT))
        original_text = ''
      else:
        original_text = ''
  return new_nodes
