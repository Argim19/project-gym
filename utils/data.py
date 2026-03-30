import json
import os


FILE_NAME = "data/clients.json"


def save_clients(client):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(client, file, indent=4, ensure_ascii=False)
    except IOError:
        print("error saving file")


def load_clients():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except (IOError, json.JSONDecodeError):
        print("error loading file")
        return []
