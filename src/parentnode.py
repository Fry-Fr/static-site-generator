from htmlnode import HTMLNode
from typing import Optional

class ParentNode(HTMLNode):
  def __init__(self, tag: str, children: list['HTMLNode'], props: Optional[dict[str, str]] = None):
    super().__init__(tag, None, children, props)

  def to_html(self) -> str:
    if not self.tag:
      raise ValueError("Error: ParentNode must have a tag to convert to HTML")
    if not self.children:
      raise ValueError("Error: ParentNode must have children to convert to HTML")
    return f"<{self.tag}{self.props_to_html()}>" + \
           "".join(child.to_html() for child in self.children) + \
           f"</{self.tag}>"
