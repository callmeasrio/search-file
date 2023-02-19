import os
import sys

def search_file(file_name):
    if sys.platform == "win32":
        root_dir = "C:\\"
    else:
        root_dir = "/"
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if name == file_name:
                print(os.path.join(root, name))

file_to_search = input("Enter the name of the file to search: ")
search_file(file_to_search)
