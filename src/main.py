from textnode import *
from folder_file_operations import *
from generate_pages_recursive import *
import sys

def main():
    copy_directory_contents("static", "docs")
    print("Static files copied successfully!")

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
