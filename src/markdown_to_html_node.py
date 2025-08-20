import re
from src.htmlnode import HTMLNode
from src.parentnode import ParentNode
from src.markdown_to_blocks import markdown_to_blocks
from src.block_to_blocktype import block_to_blocktype, BlockType
from src.text_to_textnode import text_to_textnode
from src.textnode_to_htmlnode import text_node_to_html_node

def markdown_to_html_node(markdown: str) -> HTMLNode:
	blocks = markdown_to_blocks(markdown)
	nodes = []
	for md_block in blocks:
		block_type = block_to_blocktype(md_block)
		match block_type:
			case BlockType.PARAGRAPH:
				nodes.append(ParentNode(tag="p", children=text_to_html_children(md_block.replace('\n', ' '))))
			case BlockType.HEADING:
				md_block_split = md_block.split('\n')
				for line in md_block_split:
					level = line.count('#')
					tag = f"h{level}" if 1 <= level <= 6 else "h1"
					nodes.append(ParentNode(tag=tag, children=text_to_html_children(line.replace('#', '').strip())))
			case BlockType.CODE:
				md_block_split = md_block.split('```')
				nodes.append(ParentNode(tag="pre", children=text_to_html_children_codeblock("".join(md_block_split).lstrip('\n'))))
			case BlockType.QUOTE:
				md_block_split = md_block.split('> ')
				nodes.append(ParentNode(tag="blockquote", children=text_to_html_children("".join(md_block_split).strip())))
			case BlockType.UNORDERED_LIST:
				md_block_split = re.split(r'[*|-]', md_block.replace('\n', ''))
				nodes.append(ParentNode(tag="ul", children=[ParentNode(tag="li", children=text_to_html_children(item.strip())) for item in md_block_split if item.strip()]))
			case BlockType.ORDERED_LIST:
				md_block_split = re.split(r'\d+\.\s', md_block.replace('\n', ''))
				nodes.append(ParentNode(tag="ol", children=[ParentNode(tag="li", children=text_to_html_children(item.strip())) for item in md_block_split if item.strip()]))
					
	return ParentNode(tag="div", children=nodes)

def text_to_html_children(text: str) -> list[HTMLNode]:
	text_nodes = text_to_textnode(text)
	html_nodes = []
	for node in text_nodes:
		html_nodes.append(text_node_to_html_node(node))
	return html_nodes

def text_to_html_children_codeblock(text: str) -> list[HTMLNode]:
	text_nodes = text_to_textnode(f"`{text}`")
	html_nodes = []
	for node in text_nodes:
		html_nodes.append(text_node_to_html_node(node))
	return html_nodes
