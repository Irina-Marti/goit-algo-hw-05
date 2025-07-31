#Decorator for add_contact
def inner_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Not enough arguments'
        except KeyError as e:
            if str(e) == "'Contact already exists'":
                return 'This contact already exists. Please add a new name.'
            return 'Contact not found'
    return inner

@inner_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@inner_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise IndexError('Not enough arguments')
    name, phone = args
    if name in contacts:
        raise KeyError("Contact already exists")
    contacts[name] = phone
    return f"The contact {name} added successfully"
    #else:
        #return f"The contact {name} already exists. Please enter a new name."

@inner_error
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        raise KeyError("Contact not found")
    contacts[name] = new_phone
    return f"Phone number for {name} was changed."
    #else:
       # return f"Contact {name} not found."

@inner_error
def show_phone(args, contacts):
    #if not args:
        #return "The list is empty. Please add names to it."
    name = args [0]
    #if name in contacts:
    return f"{name}: {contacts[name]}"
    #else:
        #return f"Contact {name} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()