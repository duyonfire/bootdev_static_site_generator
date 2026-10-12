from block_types import *
from htmlnode import *
from extract_title import *
import os

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	with open(from_path, "r") as file:
		from_contents = file.read()
	with open(template_path, "r") as file:
		template_contents = file.read()
	html_contents = markdown_to_html_node(from_contents)
	string_contents = html_contents.to_html()
	h1_title = extract_title(from_contents)
	actual_contents = template_contents.replace("{{ Title }}", h1_title)
	actual_contents = actual_contents.replace("{{ Content }}", string_contents)
	actual_contents = actual_contents.replace('href="/', 'href="{basepath}')
	actual_contents = actual_contents.replace('src="/', 'src="{basepath}')
	directory_path = os.path.dirname(dest_path)
	os.makedirs(directory_path, exist_ok=True)
	with open(dest_path, "w") as file:
		file.write(actual_contents)

