# Write an address book, using dictionaries, where I can query contact info,
# insert new contact, delete contact information, exit address book program
# TODO add view and more features
adress_book = {
    'Nazar': 380635895874,
    'Olexii': 380675422535,
    'Danyl': 380983651428
}
while True:
    print('Options: get, add, delete, exit')
    command = input('Enter the command: ')
    if command == 'get':
        get_contact = input('Enter the name: ')
        print(get_contact, adress_book.get(get_contact, 'No such contact in this book'))
    if command == 'add':
        add_contact = input('Enter the name and number with space between of them: ').split()
        adress_book[add_contact[0]] = int(add_contact[1])
        print(f'New contact {add_contact[0]}: {add_contact[1]} was added to this book')
    if command == 'delete':
        del_contact = input('Enter the contact to delete: ')
        del adress_book[del_contact]
        print(f'The {del_contact} was successfully deleted')
    if command == 'exit':
        break


