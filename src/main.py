import contacts


def main(filename: str = None) -> int:
    contacts.run(filename)
    return 0


if __name__ == "__main__":
    import os
    main_dir_path = os.path.dirname(os.path.abspath(__file__))
    main(os.path.join(main_dir_path, "contacts.json"))
