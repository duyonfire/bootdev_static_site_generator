import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
	def test_props_to_html(self):
		node = HTMLNode(
			"a",
			"Google",
			None,
			{
				"href": "https://www.google.com",
				"target": "_blank",
			},
		)

		self.assertEqual(
			node.props_to_html(),
			' href="https://www.google.com" target="_blank"',
		)

	def test_props_none(self):
		node = HTMLNode("p", "Hello world")

		self.assertEqual(node.props_to_html(), "")

	def test_props_empty(self):
		node = HTMLNode("p", "Hello world", None, {})

		self.assertEqual(node.props_to_html(), "")

	def test_single_prop(self):
		node = HTMLNode(
			"a",
			"Boot.dev",
			None,
			{"href": "https://www.boot.dev"},
		)

		self.assertEqual(
			node.props_to_html(),
			' href="https://www.boot.dev"',
		)

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode(
			"a",
			"Click me!",
			{"href": "https://www.google.com"}
		)
		self.assertEqual(
			node.to_html(),
			'<a href="https://www.google.com">Click me!</a>'
		)

	def test_leaf_to_html_b(self):
		node = LeafNode("b", "Bold text")
		self.assertEqual(node.to_html(), "<b>Bold text</b>")

	def test_leaf_to_html_raw_text(self):
		node = LeafNode(None, "Just some text")
		self.assertEqual(node.to_html(), "Just some text")

	def test_leaf_to_html_multiple_props(self):
		node = LeafNode(
			"a",
			"Boot.dev",
			{
				"href": "https://www.boot.dev",
				"target": "_blank"
			}
		)
		self.assertEqual(
			node.to_html(),
			'<a href="https://www.boot.dev" target="_blank">Boot.dev</a>'
		)

	def test_leaf_no_value(self):
		node = LeafNode("p", None)

		with self.assertRaises(ValueError):
			node.to_html()

	def test_leaf_repr(self):
		node = LeafNode("p", "Hello", {"class": "text"})
		self.assertEqual(
			repr(node),
			"LeafNode(tag=p, value=Hello, props={'class': 'text'})"
		)

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

	def test_to_html_with_multiple_children(self):
		parent_node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)

		self.assertEqual(
			parent_node.to_html(),
			"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
		)

	def test_to_html_with_props(self):
		child_node = LeafNode(None, "Click me")
		parent_node = ParentNode(
			"a",
			[child_node],
			{"href": "https://www.google.com"},
		)

		self.assertEqual(
			parent_node.to_html(),
			'<a href="https://www.google.com">Click me</a>',
		)

	def test_to_html_missing_tag(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode(None, [child_node])

		with self.assertRaises(ValueError):
			parent_node.to_html()

	def test_to_html_missing_children(self):
		parent_node = ParentNode("div", None)

		with self.assertRaises(ValueError):
			parent_node.to_html()

	def test_to_html_deeply_nested(self):
		node = ParentNode(
			"div",
			[
				ParentNode(
					"section",
					[
						ParentNode(
							"p",
							[
								LeafNode("b", "Deep text"),
							],
						),
					],
				),
			],
		)

		self.assertEqual(
			node.to_html(),
			"<div><section><p><b>Deep text</b></p></section></div>",
		)

if __name__ == "__main__":
	unittest.main()
