'''
This module contains functions related to commands.
'''
from contacts.load_and_save import save_contacts
from contacts.utils import list_contacts, search_contacts, clear_screen
from contacts.modifications import add_contact, delete_contact, update_contact
from contacts.modifications import update_contact_ids

VALID_COMMANDS = {"add", "delete", "update", "list", "search", "commands",
                  "clear", "quit"}

                  
def ask_command() -> str:
    command = input("Type a command: ").strip().lower()
    while command not in VALID_COMMANDS:
        print("That is not a valid command. Please try again.", end="\n\n")
        command = input("Type a command: ").strip().lower()
    return command


def display_commands() -> None:
    print("The following is a list of usable commands:")
    print('"add":      Adds a contact.')
    print('"delete":   Deletes a contact.')
    print('"update":   Updates a contact.')
    print('"list":     Lists all contacts.')
    print('"search":   Searches for a contact by name.')
    print('"commands": Display all usable commands.')
    print('"clear":    Clear screen.')
    print('"quit":     Quits the program and saves the contact list.')


def do_command(command: str, contacts: dict) -> None:
    if command == "add":
        successful = add_contact(contacts)
        if successful:
            print("Contact added.")
        else:
            print("Could not add contact.")

    elif command == "delete":
        successful = delete_contact(contacts)
        if successful:
            print("Contact deleted.")
            update_contact_ids(contacts)  # Necessary to adjust the contact IDs
        else:
            print("Could not delete contact.")

    elif command == "update":
        successful = update_contact(contacts)
        if successful:
            print("Contact updated.")
        else:
            print("Could not update contact.")

    elif command == "list":
        list_contacts(contacts)

    elif command == "search":
        matches = search_contacts(contacts)
        num_matches = len(matches)
        suffix = '' if num_matches == 1 else 's'
        print(f"Found {num_matches} matching contact{suffix}.")
        list_contacts(matches)

    elif command == "commands":
        display_commands()

    elif command == "clear":
        clear_screen()

    elif command == "quit":
        successful = save_contacts(contacts)
        if successful:
            print("Contacts were saved successfully.")
        else:
            print("Error saving contacts. Reverting to last save.")
