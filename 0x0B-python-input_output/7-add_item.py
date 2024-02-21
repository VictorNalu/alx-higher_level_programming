#!/usr/bin/python3

from sys import argv

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def main():

    # Extract command-line arguments excluding the script name
    arguments = argv[1:]

    """Load existing items from add_item.json
    if it exists, otherwise initialize an empty list
    """

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
