'''
This module contains utility functions such.
'''
import os


def display_welcome() -> None:
    print("Welcome to you contact list!")


def ask_yes_or_no(prompt: str) -> bool:
    '''
    Returns True if the user answers yes, else return False.
    '''
    true_vals = {"yes", "y"}
    false_vals = {"no", "n"}
    while True:
        ans = input(prompt).strip().lower()
        if ans in true_vals:
            return True
        elif ans in false_vals:
            return False
        else:
            print("Invalid choice, try again. Valid choices: yes or no.")


def list_contacts(contacts: dict) -> None:
    if not contacts:
        print("Contact list is empty.")
        return None

    sorted_contacts = sort_contacts(contacts)
    for i, contact in enumerate(sorted_contacts):
        first_name = contacts[contact]["first_name"]
        last_name = contacts[contact]["last_name"]
        mobile_phone_num = contacts[contact]["mobile_phone_number"]
        home_phone_num = contacts[contact]["home_phone_number"]
        email_address = contacts[contact]["email_address"]
        address = contacts[contact]["address"]

        print(f"{i + 1}. {last_name}, {first_name}")
        if mobile_phone_num:
            print(f"\tMobile Phone Number: {mobile_phone_num}")
        if home_phone_num:
            print(f"\tHome Phone Number: {home_phone_num}")
        if email_address:
            print(f"\tEmail Address: {email_address}")
        if address:
            print(f"\tAddress: {address}")


def sort_contacts(contacts: dict) -> list:
    '''
    Returns a sorted object of the contacts' keys based on alphabetic order
    (sorted by last name then by first name).
    '''
    sorted_contacts = sorted(contacts,
                             key=lambda s: (contacts[s]["last_name"].lower(),
                                            contacts[s]["first_name"].lower()))
    return list(sorted_contacts)


def search_contacts(contacts: dict, first_name: str = None,
                    last_name: str = None, exact: bool = False) -> dict:
    '''
    Search through contacts based on first and last names. This function
    can search for either exact matches or not necessarily exact matches.
    '''
    if not first_name:
        first_name = input("First name: ").strip()
    if not last_name:
        last_name = input("Last name: ").strip()

    matches = {}
    first_name = first_name.lower()
    last_name = last_name.lower()

    for contact_id, contact in contacts.items():
        contact_first_name = contact["first_name"].lower()
        contact_last_name = contact["last_name"].lower()

        if exact:
            if first_name == contact_first_name \
                    and last_name == contact_last_name:
                matches[contact_id] = contact
        else:
            if first_name in contact_first_name \
                    and last_name in contact_last_name:
                matches[contact_id] = contact

    return matches


def clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("Unsupported OS.")
