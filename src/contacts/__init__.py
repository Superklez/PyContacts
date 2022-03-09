from contacts.utils import display_welcome
from contacts.load_and_save import load_contacts
from contacts.commands import display_commands, ask_command, do_command


def run(filename: str = None) -> None:
    try:
        contacts = load_contacts(filename)
    except ValueError as error:
        print(error)
        return None
        
    display_welcome()
    print()
    display_commands()

    while True:
        print()
        command = ask_command()
        do_command(command, contacts)

        if command == "quit":
            print("Goodbye!")
            break
