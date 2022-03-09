# PyContacts

This is a console application written in Python that allows you to manage
your contact list and store it persistently in you computer. This project was
done as part of the [ProgrammingExpert](https://www.programmingexpert.io/)
course. If not specified in `main.py`, the contact list will be saved in the
same folder as `main.py` with the name `contacts.json`.

The contact list is stored as a dictionary of the format:
```
{"contact_id": {"first_name": ...,
                "last_name": ...,
                "mobile_phone_number": ...,
                "home_phone_number": ...,
                "email_address": ...,
                "address": ...},
 ...}
```
where `contact_id` is a natural number (1, 2, 3, ...). Each contact is
required to provide the fields for `first_name` and `last_name`. All other
fields are optional.

The following is a list of usable commands:
- `add`: Adds a contact.
- `delete`: Deletes a contact.
- `update`: Updates a contact.
- `list`: Lists all contacts.
- `search`: Searches for a contact by name.
- `commands`: Display all usable commands.
- `clear`: Clear screen.
- `quit`: Quits the program and saves the contact list.

Any modifications to the contact list is saved only when the `quit` command
is used. No two contacts can have the exact same first name and last name.
The `list` command prints all contacts in the contact list in alphabetical
order (first by the last name then by the first name).

When adding a new contact, various validations are performed. For more
details on what makes a contact valid, please see `src/contacts/validation.py`.
