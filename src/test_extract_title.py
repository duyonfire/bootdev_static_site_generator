import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
	def test_basic_h1(self):
		self.assertEqual(extract_title("# Hello"), "Hello")

	def test_h1_with_whitespace(self):
		self.assertEqual(extract_title("#   Hello World   "), "Hello World")

	def test_h1_in_multiline_markdown(self):
		markdown = "Some text\n# My Title\nMore text"
		self.assertEqual(extract_title(markdown), "My Title")

	def test_h1_after_other_headings(self):
		markdown = "## Subtitle\n### Section\n# Main Title"
		self.assertEqual(extract_title(markdown), "Main Title")

	def test_multiple_h1(self):
		markdown = "# First Title\n# Second Title"
		self.assertEqual(extract_title(markdown), "First Title")

	def test_no_h1(self):
		markdown = "## Subtitle\n### Section\nSome text"
		with self.assertRaises(Exception):
			extract_title(markdown)

	def test_empty_markdown(self):
		with self.assertRaises(Exception):
			extract_title("")

	def test_h1_without_space(self):
		with self.assertRaises(Exception):
			extract_title("#Hello")

	def test_h1_with_trailing_hash(self):
		self.assertEqual(extract_title("# Hello #"), "Hello #")

	def test_empty_h1_before_valid_h1(self):
		markdown = "#   \n## Subtitle\n# Actual Title"
		self.assertEqual(extract_title(markdown), "Actual Title")


if __name__ == "__main__":
	unittest.main()
