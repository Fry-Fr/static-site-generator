from typing import Optional

class HTMLNode:
  def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, children: Optional[list['HTMLNode']] = None, props: Optional[dict[str, Optional[str]]] = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError("Error: to_html method must be implemented by subclasses")
  
  def props_to_html(self) -> str:
    if self.props is None:
      return ""
    props_html = ""
    for key, value in self.props.items():
      props_html += f' {key}="{value}"'
    return props_html

  def __eq__(self, value):
    if not isinstance(value, HTMLNode):
      return False
    return (self.tag == value.tag and
            self.value == value.value and
            self.children == value.children and
            self.props == value.props)

  def __repr__(self):
    return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
