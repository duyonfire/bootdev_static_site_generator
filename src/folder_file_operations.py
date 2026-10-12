import os
import shutil

def copy_directory_contents(source: str, destination: str) -> None:
	if not (os.path.exists(source)):
		raise Exception("source path does not exist")
	if os.path.exists(destination):
		shutil.rmtree(destination)
	os.mkdir(destination)

	copy_directory_contents_r(source, destination)

def copy_directory_contents_r(source: str, destination: str) -> None:
	for i in os.listdir(source):
		actual_path = os.path.join(source, i)
		if os.path.isfile(actual_path):
			shutil.copy(actual_path, destination)
		else:
			directory_path = os.path.join(destination, i)
			os.mkdir(directory_path)
			copy_directory_contents_r(actual_path ,directory_path)
