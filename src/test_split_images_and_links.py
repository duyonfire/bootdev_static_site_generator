import unittest

from textnode import TextNode, TextType
from split_delimiter import *

class TestSplitNodesImage(unittest.TestCase):
	def test_split_single_image(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
			TextType.TEXT,
		)

		new_nodes = split_nodes_image([node])

		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode(
					"image",
					TextType.IMAGES,
					"https://i.imgur.com/zjjcJKZ.png",
				),
			],
			new_nodes,
		)

	def test_split_multiple_images(self):
		node = TextNode(
			"This is text with an ![image](image.png) and another ![second image](image2.png)",
			TextType.TEXT,
		)

		new_nodes = split_nodes_image([node])

		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGES, "image.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode("second image", TextType.IMAGES, "image2.png"),
			],
			new_nodes,
		)

	def test_split_image_at_start(self):
		node = TextNode(
			"![image](image.png) some text",
			TextType.TEXT,
		)

		new_nodes = split_nodes_image([node])

		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGES, "image.png"),
				TextNode(" some text", TextType.TEXT),
			],
			new_nodes,
		)

	def test_split_image_at_end(self):
		node = TextNode(
			"some text ![image](image.png)",
			TextType.TEXT,
		)

		new_nodes = split_nodes_image([node])

		self.assertListEqual(
			[
				TextNode("some text ", TextType.TEXT),
				TextNode("image", TextType.IMAGES, "image.png"),
			],
			new_nodes,
		)

	def test_split_image_only(self):
		node = TextNode(
			"![image](image.png)",
			TextType.TEXT,
		)

		new_nodes = split_nodes_image([node])

		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGES, "image.png"),
			],
			new_nodes,
		)

	def test_split_no_images(self):
		node = TextNode(
			"This is just normal text",
			TextType.TEXT,
		)

		new_nodes = split_nodes_image([node])

		self.assertListEqual(
			[
				node,
			],
			new_nodes,
		)

	def test_split_multiple_nodes(self):
		node1 = TextNode(
			"Hello ![cat](cat.png)",
			TextType.TEXT,
		)

		node2 = TextNode(
			"Goodbye ![dog](dog.png)",
			TextType.TEXT,
		)

		new_nodes = split_nodes_image([node1, node2])

		self.assertListEqual(
			[
				TextNode("Hello ", TextType.TEXT),
				TextNode("cat", TextType.IMAGES, "cat.png"),
				TextNode("Goodbye ", TextType.TEXT),
				TextNode("dog", TextType.IMAGES, "dog.png"),
			],
			new_nodes,
		)

	def test_split_single_link(self):
		node = TextNode(
			"This is text with a [link](https://boot.dev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("link", TextType.LINKS, "https://boot.dev"),
			],
			new_nodes,
		)

	def test_split_multiple_links(self):
		node = TextNode(
			"This has [Google](https://google.com) and [Boot.dev](https://boot.dev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This has ", TextType.TEXT),
				TextNode("Google", TextType.LINKS, "https://google.com"),
				TextNode(" and ", TextType.TEXT),
				TextNode("Boot.dev", TextType.LINKS, "https://boot.dev"),
			],
			new_nodes,
		)

	def test_split_link_at_start(self):
		node = TextNode(
			"[Boot.dev](https://boot.dev) is cool",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("Boot.dev", TextType.LINKS, "https://boot.dev"),
				TextNode(" is cool", TextType.TEXT),
			],
			new_nodes,
		)

	def test_split_link_at_end(self):
		node = TextNode(
			"Visit [Boot.dev](https://boot.dev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("Visit ", TextType.TEXT),
				TextNode("Boot.dev", TextType.LINKS, "https://boot.dev"),
			],
			new_nodes,
		)

	def test_split_link_only(self):
		node = TextNode(
			"[Boot.dev](https://boot.dev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("Boot.dev", TextType.LINKS, "https://boot.dev"),
			],
			new_nodes,
		)

	def test_split_no_links(self):
		node = TextNode(
			"This is normal text",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				node,
			],
			new_nodes,
		)

	def test_split_multiple_link_nodes(self):
		node1 = TextNode(
			"Go to [Google](https://google.com)",
			TextType.TEXT,
		)
		node2 = TextNode(
			"Go to [Boot.dev](https://boot.dev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node1, node2])
		self.assertListEqual(
			[
				TextNode("Go to ", TextType.TEXT),
				TextNode("Google", TextType.LINKS, "https://google.com"),
				TextNode("Go to ", TextType.TEXT),
				TextNode("Boot.dev", TextType.LINKS, "https://boot.dev"),
			],
			new_nodes,
		)
if __name__ == "__main__":
	unittest.main()
