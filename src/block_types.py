from enum import Enum
from markdown_to_blocks import *
from split_delimiter import *
from htmlnode import *
import re

class BlockType(Enum):
	PARAGRAPH = 'paragraph'
	HEADING = 'heading'
	CODE = 'code'
	QUOTE = 'quote'
	UNORDERED_LIST = 'unordered_list'
	ORDERED_LIST = 'ordered_list'

def block_to_block_type(markdown: str) -> BlockType:
	# Heading
	if re.findall(r"^#{1,6} .+$", markdown):
		return BlockType.HEADING
	# Code
	elif markdown.startswith("```\n") and markdown.endswith("```"):
		return BlockType.CODE
	# Quote
	lines = markdown.split("\n")
	quote: bool = True
	for i in lines:
		if not i.startswith('>'):
			quote = False
			break
	if quote == True:
		return BlockType.QUOTE
	# Unordered list
	if all(line.startswith("- ") for line in lines):
		return BlockType.UNORDERED_LIST
	# Ordered list
	ordered_list: bool = True
	for i, v in enumerate(lines):
		if not v.startswith(f'{i+1}. '):
			ordered_list = False
			break
	if ordered_list == True:
		return BlockType.ORDERED_LIST
	return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str):
	markdown_blocks = markdown_to_blocks(markdown)
	nodes = []
	for i in markdown_blocks:
		# determine block type
		block_type = block_to_block_type(i)
		# create html node
		if block_type == BlockType.PARAGRAPH:
			text = i.replace("\n", " ")
			children = text_to_children(text)
			node = ParentNode("p", children)

		elif block_type == BlockType.HEADING:
			heading_level = len(i) - len(i.lstrip('#'))
			tag = f"h{heading_level}"
			text = i.lstrip('#').strip()
			children = text_to_children(text)
			node = ParentNode(tag, children)

		elif block_type == BlockType.CODE:
			text = i[4:-3]
			code_text_node = TextNode(text, TextType.CODE_TEXT)
			code_node = text_node_to_html_node(code_text_node)
			node = ParentNode("pre", [code_node])

		elif block_type == BlockType.QUOTE:
			lines = i.split("\n")
			text = ""
			for line in lines:
				text += line.lstrip(">").strip() + " "
			text = text.strip()
			children = text_to_children(text)
			node = ParentNode("blockquote", children)

		elif block_type == BlockType.UNORDERED_LIST:
			lines = i.split("\n")
			list_items = []

			for line in lines:
				text = line.lstrip('-').strip()
				children = text_to_children(text)
				list_node = ParentNode("li", children)
				list_items.append(list_node)
			node = ParentNode("ul", list_items)

		elif block_type == BlockType.ORDERED_LIST:
			lines = i.split("\n")
			list_items = []

			for index, line in enumerate(lines):
				text = line.lstrip(f'{index + 1}.').strip()
				children = text_to_children(text)
				list_node = ParentNode("li", children)
				list_items.append(list_node)
			node = ParentNode("ol", list_items)
		nodes.append(node)
	return ParentNode("div", nodes)

# helper functions
def text_to_children(text: str):
	text_nodes = text_to_textnodes(text)
	children = []

	for node in text_nodes:
		# convert node into an HTML node
		children.append(text_node_to_html_node(node))

	return children
