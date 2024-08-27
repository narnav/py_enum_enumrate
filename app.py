import os
from enum import Enum
import json

contacts=[]
filename ="myContact.json"
class Selection(Enum):
    ADD = 1
    DELETE = 2
    SHOW = 3
    EXIT = 4
    CLEAR =5
    EDIT =6
    SEARCH =7


def menu():
    for item in Selection: print(f'{item.value} -  {item.name}')
    return   Selection(int( input("your selection?")))

def search(action):
    contactToSearch=input(f"contact To {action}?")
    for i,contact in enumerate(contacts):
        if contact["fName"] == contactToSearch:
            print(f'{contact} in {i} place')
            return i
        
    print("not found")
    return -1

def del_contact():
    search= search('delete') 
    if search >-1:del contacts[search]

# Function to save contacts to a JSON file
def save_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)  # Write the contacts list to the file with pretty-printing

def exit_app():
    save_contacts_to_file(filename,contacts)
    exit()

# Function to load contacts from a JSON file
def load_contacts_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)  # Load the contacts list from the file
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
        return []  # Return an empty list if JSON decoding fails

if __name__ =="__main__":
    contacts= load_contacts_from_file(filename)
    while True:
        userSelection =menu()
        if userSelection == Selection.EXIT: exit_app()
        if userSelection == Selection.SHOW: print(contacts)
        if userSelection == Selection.CLEAR: os.system('cls')
        if userSelection == Selection.ADD: contacts.append({'fName':input("your name?"),'age':int(input("your age?"))})
        if userSelection == Selection.SEARCH : search('search')
        if userSelection == Selection.DELETE : del_contact()
        if userSelection == Selection.EDIT : pass
