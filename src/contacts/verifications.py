from contacts.fields import get_fields
from contacts.utils import search_contacts

FIELDS = get_fields()

          
def verify_contact(contact: dict) -> bool:
    '''
    Checks if a contact is valid. The passed contact must have the following
    keys:
        - first_name
        - last_name
        - mobile_phone_num
        - home_phone_num
        - email_address
        - address
    '''
    valid = True

    for field in FIELDS:
        # First name is a required field.
        if field == "first_name" and not contact[field]:
            print("Invalid information. First name was not provided.")
            return not valid

        # Last name is a required field.
        elif field == "last_name" and not contact[field]:
            print("Invalid information. Last name was not provided.")
            return not valid

        # Check if mobile phone number is valid
        elif field == "mobile_phone_number" or field == "home_phone_number":
            # Only verify the phone number if there is one.
            if contact[field] and not verify_phone_number(contact[field]):
                print(f"Invalid {' '.join(field.split('_'))}.")
                return not valid

        # Check if email address is valid
        elif field == "email_address" and contact[field] \
                and not verify_email_address(contact[field]):
            print("Invalid email address.")
            return not valid

        # Check if address is valid
        elif field == "address" and contact[field] \
                and not verify_address(contact[field]):
            print("Invalid address.")
            return not valid

    return valid


def verify_phone_number(phone_number: str) -> bool:
    '''
    Checks if passed argument is a valid phone number. Valid phone numbers take
    the format:
    123-123-1234
    '''
    valid = True
    phone_num_split = phone_number.split('-')

    if len(phone_num_split) != 3:
        return not valid

    for i, digits in enumerate(phone_num_split):
        if not digits.isdigit():
            return not valid
        elif (i == 0 or i == 1) and len(digits) != 3:
            return not valid
        elif i == 2 and len(digits) != 4:
            return not valid

    return valid


def verify_email_address(email_address: str) -> bool:
    '''
    Checks if the passed argument is a valid email address. Valid email
    addresses take the format:
    prefix@suffix.alpha
    '''
    valid = True
    if any(not c.isalnum() and c != '@' and c != '.' for c in email_address):
        return not valid
    elif email_address.count('@') != 1:
        return not valid
    elif email_address[0] == '@' or email_address[-1] == '@':
        return not valid

    suffix = email_address.split('@')[-1]
    if suffix.count('.') == 0:
        return not valid
    elif suffix[0] == '.' or suffix[-1] == '.':
        return not valid
    elif not suffix.split('.')[-1].isalpha():
        return not valid

    return valid


def verify_address(address: str) -> bool:
    '''
    This is a relatively simple validation test for a given address. It is
    valid only when the address contains a combination of alphanumeric
    characters, dots, commas, and spaces. There must also be at least
    one alphanumeric character.
    '''
    valid = True
    if any(not c.isalnum() and c != '.' and c != ',' and c != ' ' for c in
            address):
        return not valid
    elif any(c.isalnum() for c in address):
        return valid

    return valid


def verify_unique_contact(contact: dict, contacts: dict) -> bool:
    '''
    Checks if the contact is already in the contacts.
    '''
    first_name = contact["first_name"]
    last_name = contact["last_name"]
    unique = True

    # Unique contacts are determined by the first and last names provided.
    if search_contacts(contacts, first_name, last_name, exact=True):
        return not unique

    return unique
