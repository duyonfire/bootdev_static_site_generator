import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
	def test_markdown_to_blocks(self):
		md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)

	def test_strip_whitespace(self):
		md = """
   First block   

   Second block   
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"First block",
				"Second block",
			],
		)

	def test_excessive_newlines(self):
		md = """
First block



Second block




Third block
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"First block",
				"Second block",
				"Third block",
			],
		)

	def test_single_block(self):
		md = "Just one paragraph"
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"Just one paragraph",
			],
		)


if __name__ == "__main__":
	unittest.main()
