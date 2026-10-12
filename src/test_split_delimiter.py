import unittest

from textnode import TextNode, TextType
from split_delimiter import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
	def test_plain_text(self):
		text = "This is plain text"

		nodes = text_to_textnodes(text)

		expected = [
			TextNode("This is plain text", TextType.TEXT),
		]

		self.assertEqual(nodes, expected)

	def test_bold(self):
		text = "This is **bold** text"

		nodes = text_to_textnodes(text)

		expected = [
			TextNode("This is ", TextType.TEXT),
			TextNode("bold", TextType.BOLD_TEXT),
			TextNode(" text", TextType.TEXT),
		]

		self.assertEqual(nodes, expected)

	def test_italic(self):
		text = "This is _italic_ text"

		nodes = text_to_textnodes(text)

		expected = [
			TextNode("This is ", TextType.TEXT),
			TextNode("italic", TextType.ITALIC_TEXT),
			TextNode(" text", TextType.TEXT),
		]

		self.assertEqual(nodes, expected)

	def test_code(self):
		text = "This is `code` text"

		nodes = text_to_textnodes(text)

		expected = [
			TextNode("This is ", TextType.TEXT),
			TextNode("code", TextType.CODE_TEXT),
			TextNode(" text", TextType.TEXT),
		]

		self.assertEqual(nodes, expected)

	def test_image(self):
		text = "This is ![obi wan](https://example.com/obi.jpg) image"

		nodes = text_to_textnodes(text)

		expected = [
			TextNode("This is ", TextType.TEXT),
			TextNode(
				"obi wan",
				TextType.IMAGES,
				"https://example.com/obi.jpg"
			),
			TextNode(" image", TextType.TEXT),
		]

		self.assertEqual(nodes, expected)

	def test_link(self):
		text = "This is a [link](https://boot.dev)"

		nodes = text_to_textnodes(text)

		expected = [
			TextNode("This is a ", TextType.TEXT),
			TextNode(
				"link",
				TextType.LINKS,
				"https://boot.dev"
			),
		]

		self.assertEqual(nodes, expected)

	def test_all_types(self):
		text = (
			"This is **text** with an _italic_ word and a "
			"`code block` and an "
			"![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
			"and a [link](https://boot.dev)"
		)

		nodes = text_to_textnodes(text)

		expected = [
			TextNode("This is ", TextType.TEXT),
			TextNode("text", TextType.BOLD_TEXT),
			TextNode(" with an ", TextType.TEXT),
			TextNode("italic", TextType.ITALIC_TEXT),
			TextNode(" word and a ", TextType.TEXT),
			TextNode("code block", TextType.CODE_TEXT),
			TextNode(" and an ", TextType.TEXT),
			TextNode(
				"obi wan image",
				TextType.IMAGES,
				"https://i.imgur.com/fJRm4Vk.jpeg"
			),
			TextNode(" and a ", TextType.TEXT),
			TextNode(
				"link",
				TextType.LINKS,
				"https://boot.dev"
			),
		]

		self.assertEqual(nodes, expected)


if __name__ == "__main__":
	unittest.main()
