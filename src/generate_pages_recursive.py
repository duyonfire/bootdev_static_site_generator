import os
from generate_page import *

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
	for i in os.listdir(dir_path_content):
		actual_path = os.path.join(dir_path_content, i)
		if os.path.isfile(actual_path) and i.lower().endswith(('.md', '.markdown')):
			file_name = os.path.splitext(i)[0]
			new_file_extension = f'{file_name}.html'
			dest_file_path = os.path.join(dest_dir_path, new_file_extension)
			generate_page(actual_path, template_path, dest_file_path)
		elif os.path.isdir(actual_path):
			updated_dest_dir_path = os.path.join(dest_dir_path, i)
			generate_pages_recursive(actual_path, template_path, updated_dest_dir_path)
