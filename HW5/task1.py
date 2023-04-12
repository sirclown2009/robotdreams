# to store names and phone numbers (paired)
contacts = {}


def add_contact():
    global name_lastname
    global pnumber
    while True:
        try:
            name_lastname = input("Name: ")
            pnumber = int(input("Phone number: +380"))
        except ValueError:
            print("Please use only digits")
            # how to make the program go back to the beginning of the while loop?
            if name_lastname in contacts:
                print("You already have this contact saved")
            elif len(pnumber) == 9:
                print(f"{name_lastname} contact is saved")
            elif len(pnumber) < 9 > len(pnumber):
                print("Your number should be 9 digits long")
                pnumber = input("Phone number: +380")
                print(f"{name_lastname} contact is saved")
            contacts[name_lastname] = pnumber
        finally:
            menu()


def delete_contact():
    while True:
        name = input("Enter the name of the contact you want to delete: ")
        if name in contacts:
            del contacts[name_lastname]
            print(f"{name} contact was deleted")
            menu()
        else:
            print(f"{name} was not found")
            print("*To quit type in 'q'")
            name = input("Enter the name of the contact you want to delete: ")
            if name == "q":
                menu()


def view_contacts():
    print(contacts)
    menu()


def stats():
    print(len(contacts))
    menu()


def find_contact():
    while True:
        gui = int(input("Find by name (1) or Find by number (2): "))
        try:
            if gui == 1:
                name = input("Name: ")
                # if name in name_lastname:
                #     print(f"{contacts[name]}")
                try:
                    name_found = contacts[name]
                except KeyError:
                    print(f"Contact {name} does not exist")
                else:
                    print(name_found)
                    menu()
            if gui == 2:
                number = input("Number: ")
                try:
                    number_found = contacts[name]
                except KeyError:
                    print(f"Contact with the number {number} does not exist")
                else:
                    print(number_found)
        finally:
            print("Type in a valid number")
            menu()


def menu():
    while True:
        gui = input("""                        1. Add new contact
                        2. Delete contact
                        3. View all contacts
                        4. Find contact
                        5. Stats
                        Navigate (1, 2, 3 or 4; to quit type 'q'): """)
        if gui == "1":
            add_contact()
        elif gui == "2":
            delete_contact()
        elif gui == "3":
            view_contacts()
        elif gui == "4":
            find_contact()
        elif gui == "5":
            stats()
        elif gui == "q":
            break
        else:
            print(f"Please type valid number")


menu()