import unittest
from textnode import *
from htmlnode import *
from split_delimiter import *

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD_TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("Number 1", TextType.BOLD_TEXT)
		node2 = TextNode("Number 2", TextType.BOLD_TEXT)
		self.assertNotEqual(node, node2)

	def test_not_eq_text_type(self):
		node = TextNode("Same text", TextType.BOLD_TEXT)
		node2 = TextNode("Same text", TextType.ITALIC_TEXT)
		self.assertNotEqual(node, node2)

	def test_not_eq_url(self):
		node = TextNode("Google", TextType.LINKS, "https://google.com")
		node2 = TextNode("Google", TextType.LINKS, None)
		self.assertNotEqual(node, node2)

	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)

		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_bold(self):
		node = TextNode("This is bold", TextType.BOLD_TEXT)
		html_node = text_node_to_html_node(node)

		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is bold")

	def test_italic(self):
		node = TextNode("This is italic", TextType.ITALIC_TEXT)
		html_node = text_node_to_html_node(node)

		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is italic")

	def test_code(self):
		node = TextNode("print('hello')", TextType.CODE_TEXT)
		html_node = text_node_to_html_node(node)

		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "print('hello')")

	def test_link(self):
		node = TextNode(
			"Boot.dev",
			TextType.LINKS,
			"https://boot.dev",
		)
		html_node = text_node_to_html_node(node)

		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "Boot.dev")
		self.assertEqual(
			html_node.props,
			{"href": "https://boot.dev"},
		)

	def test_image(self):
		node = TextNode(
			"picture of a cat",
			TextType.IMAGES,
			"https://example.com/cat.jpg",
		)
		html_node = text_node_to_html_node(node)

		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(
			html_node.props,
			{
				"src": "https://example.com/cat.jpg",
				"alt": "picture of a cat",
			},
		)

	def test_bold(self):
		node = TextNode("This is **bold** text", TextType.TEXT)

		new_nodes = split_nodes_delimiter(
			[node],
			"**",
			TextType.BOLD_TEXT,
		)

		self.assertEqual(
			new_nodes,
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("bold", TextType.BOLD_TEXT),
				TextNode(" text", TextType.TEXT),
			],
		)

	def test_italic(self):
		node = TextNode("This is _italic_ text", TextType.TEXT)

		new_nodes = split_nodes_delimiter(
			[node],
			"_",
			TextType.ITALIC_TEXT,
		)

		self.assertEqual(
			new_nodes,
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC_TEXT),
				TextNode(" text", TextType.TEXT),
			],
		)

	def test_code(self):
		node = TextNode("This is `code` text", TextType.TEXT)

		new_nodes = split_nodes_delimiter(
			[node],
			"`",
			TextType.CODE_TEXT,
		)

		self.assertEqual(
			new_nodes,
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("code", TextType.CODE_TEXT),
				TextNode(" text", TextType.TEXT),
			],
		)

	def test_multiple_delimiters(self):
		node = TextNode("**a** bold **b** c", TextType.TEXT)

		new_nodes = split_nodes_delimiter(
			[node],
			"**",
			TextType.BOLD_TEXT,
		)

		self.assertEqual(
			new_nodes,
			[
				TextNode("a", TextType.BOLD_TEXT),
				TextNode(" bold ", TextType.TEXT),
				TextNode("b", TextType.BOLD_TEXT),
				TextNode(" c", TextType.TEXT),
			],
		)

	def test_delimiter_at_end(self):
		node = TextNode("hello **world**", TextType.TEXT)

		new_nodes = split_nodes_delimiter(
			[node],
			"**",
			TextType.BOLD_TEXT,
		)

		self.assertEqual(
			new_nodes,
			[
				TextNode("hello ", TextType.TEXT),
				TextNode("world", TextType.BOLD_TEXT),
			],
		)

	def test_non_text_node_unchanged(self):
		node = TextNode("already bold", TextType.BOLD_TEXT)

		new_nodes = split_nodes_delimiter(
			[node],
			"**",
			TextType.BOLD_TEXT,
		)

		self.assertEqual(
			new_nodes,
			[
				TextNode("already bold", TextType.BOLD_TEXT),
			],
		)

	def test_multiple_nodes(self):
		nodes = [
			TextNode("hello **world**", TextType.TEXT),
			TextNode("already italic", TextType.ITALIC_TEXT),
			TextNode("another **bold** part", TextType.TEXT),
		]

		new_nodes = split_nodes_delimiter(
			nodes,
			"**",
			TextType.BOLD_TEXT,
		)

		self.assertEqual(
			new_nodes,
			[
				TextNode("hello ", TextType.TEXT),
				TextNode("world", TextType.BOLD_TEXT),
				TextNode("already italic", TextType.ITALIC_TEXT),
				TextNode("another ", TextType.TEXT),
				TextNode("bold", TextType.BOLD_TEXT),
				TextNode(" part", TextType.TEXT),
			],
		)

	def test_unmatched_delimiter(self):
		node = TextNode("This is **broken", TextType.TEXT)

		with self.assertRaises(Exception):
			split_nodes_delimiter(
				[node],
				"**",
				TextType.BOLD_TEXT,
			)
if __name__ == "__main__":
	unittest.main()
