'''
This module contains functions needed to modify the contact list.
'''
from contacts.fields import get_fields
from contacts.utils import ask_yes_or_no, search_contacts
from contacts.verifications import verify_contact, verify_unique_contact

FIELDS = get_fields()


def add_contact(contacts: dict) -> bool:
    '''
    This assumes that all contact IDs are consecutive in order. Please
    use update_contact_ids when deleting a contact.
    '''
    num_contacts = len(contacts)
    successful = True
    new_contact = {}

    for field in FIELDS:
        prompt = ' '.join(s.capitalize() for s in field.split('_')) + ": "
        new_contact[field] = input(prompt).strip()

    if not verify_contact(new_contact):
        return not successful
    if not verify_unique_contact(new_contact, contacts):
        print("A contact with this name already exists.")
        return not successful

    contacts[str(num_contacts + 1)] = new_contact
    return successful


def delete_contact(contacts: dict) -> bool:
    successful = True
    first_name = input("First name: ").strip().lower()
    last_name = input("Last name: ").strip().lower()

    if not first_name:
        print("Invalid information. First name was not provided.")
        return not successful
    elif not last_name:
        print("Invalid information. Last name was not provided.")
        return not successful

    # Check is contact exists.
    match = search_contacts(contacts, first_name, last_name, exact=True)
    if not match:
        print("No matching contact found.")
        return not successful

    match_id = list(match.keys())[0]
    del contacts[match_id]

    return successful


def update_contact(contacts: dict) -> bool:
    successful = True

    # Search for contact to update and check if it exists.
    match = search_contacts(contacts, exact=True)
    if not match:
        print("No matching contact found.")
        return not successful

    # Get the contact to update
    match_id = list(match.keys())[0]
    contact_to_update = contacts[match_id]
    updated_contact = contact_to_update.copy()

    # Ask which fields to update
    for field in FIELDS:
        field_split = field.split('_')
        update_prompt = f"Update {' '.join(field_split)}? "
        input_prompt = ' '.join(s.capitalize() for s in field_split) + ": "

        if ask_yes_or_no(update_prompt):
            updated_contact[field] = input(input_prompt).strip()

    if not verify_contact(updated_contact):
        return not successful

    same_first_name = updated_contact["first_name"] == \
        contact_to_update["first_name"]
    same_last_name = updated_contact["last_name"] == \
        contact_to_update["last_name"]
    if not same_first_name or not same_last_name:
        if not verify_unique_contact(updated_contact, contacts):
            print("A contact with this name already exists.")
            return not successful

    contacts[match_id] = updated_contact
    return successful


def update_contact_ids(contacts: dict) -> None:
    '''
    This will look through all the contacts and adjust the contact ids if
    necessary. Contact IDs must start at 1. Can only handle one missing contact
    ID at a time.
    '''
    prev = 0
    missing_id = 0

    # Find the missing contact ID
    for curr in map(int, sorted(contacts)):
        if curr != prev + 1:
            missing_id = prev + 1
            break
        prev = curr

    # If no missing ID was found
    if not missing_id:
        return None

    # Adjust all contact IDs
    for i in map(int, sorted(contacts)):
        if i > missing_id:
            contacts[str(i - 1)] = contacts[str(i)]

    del contacts[max(contacts)]
