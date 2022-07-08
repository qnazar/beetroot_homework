import json
from art import text2art
from typing import Optional


def generate_response(contact: Optional[dict] = None):
    if contact:
        print('-' * 24)
        print('| {:<20} |'.format(contact['first name'] + ' ' + contact['last name']))
        print('| {:<20} |'.format(contact['phone number']))
        print('| {:<20} |'.format(contact['city']))
        print('-' * 24)
    else:
        print('No info in PhoneBook')


def add_new(data: dict) -> None:
    while True:
        first_name: str = input('First name: ')
        second_name: str = input('Last name: ')
        phone_number: str = input('Phone number: ')
        city: str = input('City: ')
        new_contact: dict = {'first name': first_name, 'last name': second_name,
                             'phone number': phone_number, 'city': city}
        generate_response(new_contact)
        confirm = input('Please, check the info. Are you sure you want to add this entry? [Y/n]: ')
        if confirm == 'Y':
            print('New entry added successfully!')
            return data['contacts'].append(new_contact)
        next_step: str = input('Do you want to try again? [Y/n]: ')
        if next_step == 'Y':
            continue
        else:
            break


def delete(request: str, data: dict) -> None:
    matched: int = 0
    for contact in data['contacts']:
        if contact['phone number'] == request:
            matched += 1
            generate_response(contact)
            confirm: str = input('Do you really want to delete all this info? [Y/n]: ')
            if confirm == 'Y':
                data['contacts'].remove(contact)
                print(f"{contact['first name']} {contact['last name']} has been removed from PhoneBook.")
            else:
                print('Deletion stopped.')
    if matched == 0:
        generate_response()


def update(request: str, data: dict) -> None:
    matched: int = 0
    for contact in data['contacts']:
        if contact['phone number'] == request:
            matched += 1
            generate_response(contact)
            print('Enter "e" to set the changes and return to main menu')
            print('Items to update:   f - first name   |   l - last name   |   c - city')
            while True:
                item: str = input('Which item do you want to update? ')
                if item == 'f':
                    new: str = input('Updated name: ')
                    contact['first name'] = new
                elif item == 'l':
                    new: str = input('Updated surname: ')
                    contact['last name'] = new
                elif item == 'c':
                    new: str = input('Updated city: ')
                    contact['city'] = new
                elif item == 'e':
                    print('This contact has been updated.')
                    generate_response(contact)
                    break
                else:
                    print('Unknown parameter')
    if matched == 0:
        generate_response()


def search_by_first_name(request: str, data: dict) -> None:
    matches = 0
    for contact in data['contacts']:
        if contact['first name'] == request:
            matches += 1
            generate_response(contact)
    if matches == 0:
        generate_response()


def search_by_last_name(request: str, data: dict) -> None:
    matches = 0
    for contact in data['contacts']:
        if contact['last name'] == request:
            matches += 1
            generate_response(contact)
    if matches == 0:
        generate_response()


def search_by_full_name(request: str, data: dict) -> None:
    matches = 0
    first_name, last_name = request.split()
    for contact in data['contacts']:
        if contact['first name'] == first_name and contact['last name'] == last_name:
            matches += 1
            generate_response(contact)
    if matches == 0:
        generate_response()


def search_by_number(request: str, data: dict) -> None:
    matches = 0
    for contact in data['contacts']:
        if request in contact['phone number']:
            matches += 1
            generate_response(contact)
    if matches == 0:
        generate_response()


def search_by_city(request: str, data: dict) -> None:
    matches: int = 0
    for contact in data['contacts']:
        if contact['city'] == request:
            matches += 1
            generate_response(contact)
    if matches == 0:
        generate_response()


def print_menu() -> None:
    print('''                                   MAIN MENU
    
- a: add new entry          - d: delete by number       - u: update by number
- s: search by first name   - l: search by last name    - f: search by full name
- n: search by number       - c: search by city         - e: exit''')


def app_run(phonebook: str) -> None:
    with open(phonebook, 'r') as file:
        data: dict = json.load(file)
    print(text2art('< < < <   PhoneBook   > > > >'), end='')
    while True:
        print_menu()
        option: str = input('\nChoose an option: ')
        if option == 's':
            request: str = input('Enter the first name: ')
            search_by_first_name(request, data)
        elif option == 'l':
            request: str = input('Enter the last name: ')
            search_by_last_name(request, data)
        elif option == 'f':
            request: str = input('Enter the full name: ')
            search_by_full_name(request, data)
        elif option == 'n':
            request: str = input('Enter the phone number: ')
            search_by_number(request, data)
        elif option == 'c':
            request: str = input('Enter the city: ')
            search_by_city(request, data)
        elif option == 'a':
            add_new(data)
        elif option == 'd':
            request: str = input('Enter phone number: ')
            delete(request, data)
        elif option == 'u':
            request: str = input('Enter phone number: ')
            update(request, data)
        elif option == 'e':
            print('Saving data...')
            print('Good bye')
            with open(phonebook, 'w') as file:
                json.dump(data, file, indent=4)
            break
        else:
            print('Unknown command')


if __name__ == '__main__':
    app_run('contacts.json')
