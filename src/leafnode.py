from htmlnode import HTMLNode
from typing import Optional

class LeafNode(HTMLNode):
  def __init__(self, tag: Optional[str], value: str, props: Optional[dict[str, Optional[str]]] = None):
    super().__init__(tag, value, None, props)

  def to_html(self) -> str:
    if not self.value:
      raise ValueError("Error: LeafNode must have a non-empty value to convert to HTML")
    if not self.tag:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"