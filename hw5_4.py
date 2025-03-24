def parse_input(user_input):
    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            # return "Give me name and phone please."
            return "We got ValueError."
        except KeyError:
            return "We got KeyError."
        except IndexError:
            return "We got IndexError."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."

    return inner

@input_error
def show_phone(args, contacts):
    return contacts[args[0]]

def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone changed to {phone}, for user {name}"
    else:
        return "Name does not exist in contacts"

def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

    if __name__ == "__main__":
        main()