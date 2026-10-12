from enum import Enum
from htmlnode import *

class TextType(Enum):
	TEXT = 'text'
	BOLD_TEXT = 'bold text'
	ITALIC_TEXT = 'italic text'
	CODE_TEXT = 'code text'
	LINKS = '[anchor text](url)'
	IMAGES = '![alt text](url)'

class TextNode:
	def __init__(self, text, text_type: TextType, url = None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
			return True
		return False

	def __repr__(self):
		return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
	tt = text_node.text_type
	if tt not in TextType:
		raise Exception("text type is not in TextType enum")
	elif tt == TextType.TEXT:
		return LeafNode(None, text_node.text)
	elif tt == TextType.BOLD_TEXT:
		return LeafNode('b', text_node.text)
	elif tt == TextType.ITALIC_TEXT:
		return LeafNode('i', text_node.text)
	elif tt == TextType.CODE_TEXT:
		return LeafNode('code', text_node.text)
	elif tt == TextType.LINKS:
		return LeafNode('a', text_node.text, {'href': text_node.url})
	elif tt == TextType.IMAGES:
		return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
