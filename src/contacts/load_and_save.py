'''
This module contains functions for loading and saving the contact list.

The format of the JSON file is as follows:
{"contact_id": {"first_name": ...,
                "last_name": ...,
                "mobile_phone_number": ...,
                "home_phone_number": ...,
                "email_address": ...,
                "address": ...},
 ...}
where contact_id is a natural number (e.g. 1, 2, 3, ...)
'''
import json

FILENAME = "contacts.json"


def load_contacts(filename: str = None) -> dict:
    global FILENAME
    if filename:
        FILENAME = filename

    if FILENAME.split('.')[-1] != "json":
        raise ValueError("Filename must end with .json extension.")

    try:
        with open(FILENAME, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        # Create file if file does not exist.
        contacts = {}
        save_contacts(contacts)

    return contacts


def save_contacts(contacts: dict) -> bool:
    successful = True
    try:
        with open(FILENAME, "w") as file:
            json.dump(contacts, file)
    except Exception as error:
        print(error)
        return not successful
    return successful
