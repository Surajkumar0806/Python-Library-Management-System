import json
import os


project_folder=os.path.dirname(__file__)
json_path=os.path.join(project_folder, "books.json")
json_member_path=os.path.join(project_folder, "members.json")

def load_books_data():
    try:
        with open(json_path, "r") as file:
            return json.load(file)
    except( FileNotFoundError, json.JSONDecodeError):
        return []

def load_members_data():
    try:
        with open(json_member_path, "r") as file:
            return json.load(file)
    except( FileNotFoundError, json.JSONDecodeError):
        return []