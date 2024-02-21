#!/usr/bin/python3
"""A module that loads, adds and saves arguments to a Python list"""

from sys import argv
from json import dump, load


def save_to_json_file(data, filename):
    with open(filename, "w") as file:
        dump(data, file)


def load_from_json_file(filename):
    with open(filename, "r") as file:
        return load(file)


def main():
    # Extract command-line arguments excluding the script name
    arguments = argv[1:]

    # Load existing items from add_item.json if it exists, otherwise initialize an empty list
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add the new arguments to the existing list
    items.extend(arguments)

    # Save the updated list to add_item.json
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()
