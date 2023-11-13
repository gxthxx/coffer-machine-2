import json

def load_menu(file_path):
    with open(file_path, 'r') as menu_file:
        return json.load(menu_file)
