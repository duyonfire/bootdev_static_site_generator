from htmlnode import *
from textnode import *
from regex_functions import *
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
	new_list = []
	for i in old_nodes:
		if i.text_type != TextType.TEXT:
			new_list.append(i)
			continue
		delimiter_count = i.text.count(delimiter)
		if delimiter_count % 2 != 0:
			raise Exception('invalid markdown syntax, no matching delimiter found')
		split_sentences = i.text.split(delimiter)
		for index, value in enumerate(split_sentences):
			if value == '':
				continue
			if index % 2 == 0:
				new_list.append(TextNode(value, TextType.TEXT))
			else:
				new_list.append(TextNode(value, text_type))
	return new_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
	my_list: list[TextNode] = []
	for i in old_nodes:
		if i.text_type != TextType.TEXT:
			my_list.append(i)
			continue

		images: list[tuple[str, str]] = extract_markdown_images(i.text)
		if len(images) == 0 and i.text != '':
			my_list.append(i)
			continue

		num_images: int = len(images)
		curr_text: str = i.text
		for v in range(num_images):
			sections: list[str] = curr_text.split(f'![{images[v][0]}]({images[v][1]})', 1)
			if sections[0] != '':
				my_list.append(TextNode(sections[0], TextType.TEXT))
			my_list.append(TextNode(images[v][0], TextType.IMAGES, images[v][1]))
			curr_text = sections[1]
		if curr_text != '':
			my_list.append(TextNode(curr_text, TextType.TEXT))
	return my_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
	my_list: list[TextNode] = []

	for i in old_nodes:
		if i.text_type != TextType.TEXT:
			my_list.append(i)
			continue

		links: list[tuple[str, str]] = extract_markdown_links(i.text)

		if len(links) == 0 and i.text != '':
			my_list.append(i)
			continue

		num_links: int = len(links)
		curr_text: str = i.text

		for v in range(num_links):
			sections: list[str] = curr_text.split(
				f'[{links[v][0]}]({links[v][1]})',
				1
			)

			if sections[0] != '':
				my_list.append(TextNode(sections[0], TextType.TEXT))

			my_list.append(
				TextNode(
					links[v][0],
					TextType.LINKS,
					links[v][1]
				)
			)

			curr_text = sections[1]

		if curr_text != '':
			my_list.append(TextNode(curr_text, TextType.TEXT))

	return my_list

def text_to_textnodes(text: str) -> list[TextNode]:
	node: list[TextNode] = [TextNode(text, TextType.TEXT)]
	node = split_nodes_delimiter(node, '**', TextType.BOLD_TEXT)
	node = split_nodes_delimiter(node, '_', TextType.ITALIC_TEXT)
	node = split_nodes_delimiter(node, "`", TextType.CODE_TEXT)
	node = split_nodes_image(node)
	node = split_nodes_link(node)
	return node
