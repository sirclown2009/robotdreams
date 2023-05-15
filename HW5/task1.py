import json
import time
# to store names and phone numbers (paired)
contacts = {}
function_call_data = {}
function_error = {}


class NotAnInteger(ValueError):
    pass


def funcname_time(func):
    def wraper():
        current_time = time.strftime("%H:%M:%S")
        function_call = {"Function name": func.__name__, "Time": current_time}
        function_call_data[name] = function_call
        with open("function_time.json", "w") as f:
            json.dump(function_call_data, f)
        with open("function_time.json", "r") as read_f:
            json.load(read_f)
        # I can't use f.write here because the argument type is not a str, how to save it then?
    return wraper



def create_contact():
    global name
    global pnumber
    while True:
        name = input("Enter the name: ")
        pnumber = input("Enter the phone number: +380")
        contact_data = {"Name": name, "Phone number": pnumber}
        contacts[name] = contact_data
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
        @funcname_time
        def show_time():
            return None

        show_time()
        if name in contact_data:
            print("You already have this contact saved")
            menu()
        elif len(pnumber) == 9:
            print(f"{name} contact is saved")
            menu()
        elif len(pnumber) < 9 or len(pnumber) > 9:
                print("Your number should be 9 digits long")
                menu()


def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        contacts.pop(name)
        print("Your contact was deleted")
        menu()


def view_contacts():
    with open("contacts.json", "r") as read_f:
        contact_data = json.load(read_f)
        print(contacts)
    menu()


def stats():
    length = len(contacts)
    print("The number of contacts is: ", length)



def find_contact():
    while True:
        try:
            gui = int(input("Find by name (1): "))
        except ValueError:
            # it does work with ve, but doesn't with custom exception. what could be the reason?
            print("The program only takes numbers as the argument\n")
            current_time = time.strftime("%H:%M:%S")
            function_call = {"Error": "NotAnInteger", "Time": current_time}
            function_error["Error occurred:"] = function_call
            with open("function_error.json", "w") as f:
                json.dump(function_error, f)
            with open("function_time.json", "r") as read_f:
                json.load(read_f)
            pass
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
        except NotAnInteger:
            print("The program accepts only integers")
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
            create_contact()
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
