from textnode import *
from folder_file_operations import *
from generate_pages_recursive import *

def main():
    print("TextNode(")
    copy_directory_contents("static", "public")
    print("Static files copied successfully!")
    generate_pages_recursive("content", "template.html", "public")

main()
