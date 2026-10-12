import unittest

from regex_functions import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual(
			[("image", "https://i.imgur.com/zjjcJKZ.png")],
			matches
		)

	def test_extract_multiple_markdown_images(self):
		matches = extract_markdown_images(
			"This has ![cat](cat.png) and ![dog](dog.jpg)"
		)
		self.assertListEqual(
			[
				("cat", "cat.png"),
				("dog", "dog.jpg"),
			],
			matches
		)

	def test_extract_markdown_images_no_matches(self):
		matches = extract_markdown_images(
			"This text has no markdown images"
		)
		self.assertListEqual([], matches)

	def test_extract_markdown_image_empty_alt_text(self):
		matches = extract_markdown_images(
			"This has an image ![](image.png)"
		)
		self.assertListEqual(
			[("", "image.png")],
			matches
		)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
			"This is text with a link [to boot dev](https://www.boot.dev)"
		)
		self.assertListEqual(
			[("to boot dev", "https://www.boot.dev")],
			matches
		)

	def test_extract_multiple_markdown_links(self):
		matches = extract_markdown_links(
			"This has [Google](https://google.com) and [Boot.dev](https://boot.dev)"
		)
		self.assertListEqual(
			[
				("Google", "https://google.com"),
				("Boot.dev", "https://boot.dev"),
			],
			matches
		)

	def test_extract_markdown_links_no_matches(self):
		matches = extract_markdown_links(
			"This text has no markdown links"
		)
		self.assertListEqual([], matches)

	def test_extract_links_does_not_extract_images(self):
		matches = extract_markdown_links(
			"This is ![cat](cat.png)"
		)
		self.assertListEqual([], matches)

	def test_extract_images_does_not_extract_links(self):
		matches = extract_markdown_images(
			"This is [cat](cat.png)"
		)
		self.assertListEqual([], matches)


if __name__ == "__main__":
	unittest.main()
