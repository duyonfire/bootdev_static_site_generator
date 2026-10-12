import unittest

from block_types import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
	def test_paragraph(self):
		md = """This is **bolded** paragraph
text in a p
tag here"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
		)

	def test_heading_1(self):
		md = "# Hello world"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><h1>Hello world</h1></div>",
		)

	def test_heading_2(self):
		md = "## Second heading"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><h2>Second heading</h2></div>",
		)

	def test_heading_6(self):
		md = "###### Small heading"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><h6>Small heading</h6></div>",
		)

	def test_heading_with_bold(self):
		md = "### Hello **world**"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><h3>Hello <b>world</b></h3></div>",
		)

	def test_heading_with_italic(self):
		md = "#### This is _italic_"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><h4>This is <i>italic</i></h4></div>",
		)

	def test_quote(self):
		md = "> This is a quote"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><blockquote>This is a quote</blockquote></div>",
		)

	def test_multiline_quote(self):
		md = """> This is line one
> This is line two"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><blockquote>This is line one This is line two</blockquote></div>",
		)

	def test_quote_with_bold(self):
		md = "> This is **bold** text"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><blockquote>This is <b>bold</b> text</blockquote></div>",
		)

	def test_quote_with_italic(self):
		md = "> This is _italic_ text"

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><blockquote>This is <i>italic</i> text</blockquote></div>",
		)

	def test_codeblock(self):
		md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
		)

	def test_unordered_list(self):
		md = """- Apple
- Banana
- Orange"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><ul><li>Apple</li><li>Banana</li><li>Orange</li></ul></div>",
		)

	def test_unordered_list_with_inline_markdown(self):
		md = """- **Apple**
- _Banana_
- `Orange`"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><ul><li><b>Apple</b></li><li><i>Banana</i></li><li><code>Orange</code></li></ul></div>",
		)

	def test_ordered_list(self):
		md = """1. Apple
2. Banana
3. Orange"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><ol><li>Apple</li><li>Banana</li><li>Orange</li></ol></div>",
		)

	def test_ordered_list_with_inline_markdown(self):
		md = """1. **First**
2. _Second_
3. `Third`"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><ol><li><b>First</b></li><li><i>Second</i></li><li><code>Third</code></li></ol></div>",
		)

	def test_full_document(self):
		md = """# My Page

This is a **paragraph** with _italic_ text.

> This is a quote

- Apple
- Banana

1. First
2. Second"""

		node = markdown_to_html_node(md)

		self.assertEqual(
			node.to_html(),
			"<div><h1>My Page</h1><p>This is a <b>paragraph</b> with <i>italic</i> text.</p><blockquote>This is a quote</blockquote><ul><li>Apple</li><li>Banana</li></ul><ol><li>First</li><li>Second</li></ol></div>",
		)


if __name__ == "__main__":
	unittest.main()
