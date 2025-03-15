
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]"
    
    name, phone = args
    if name in contacts:
        return f'Name {name} already exists in contacts!'
    contacts[name] = phone
    return "Contact added."

def show_all(contacts):
    if len(contacts) == 0:
        return 'Contact list is empty'   
    
    result = []
    for contact in contacts:
        result.append(f'{contact}: {contacts[contact]}')
    return '\n'.join(result)

def change_contact(args, contacts):
        if len(args) != 2:
            return "Invalid command format. Use: add [name] [new phone]"

        name, phone = args
        if name not in contacts:
            return f'There are no contacts with name {name}'
        
        contacts[name] = phone
        return 'Contact changed.'
    

def phone_user(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"
    
    name = args[0]
    if name not in contacts:
        return f'There are no contacts with name {name}'
    
    return contacts[name]


def main():
    contacts = {'Vi': 345,
                'Dsa': 45346}
    # contacts = {'Vi': 4535,}
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
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(phone_user(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")



if __name__ == '__main__':
    main()