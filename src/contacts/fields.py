'''
This module contains the fields in every contact.
'''
FIELDS = ["first_name", "last_name", "mobile_phone_number",
          "home_phone_number", "email_address", "address"]


def get_fields() -> list:
    return FIELDS[:]
