phonebook = {
    'John': '12 22 33 44',
    'Evelynn': '13 22 33 44',
    'Leo': '13 22 73 47',
    'Henrik': '13 82 73 87',
    'Arthur': '13 99 73 87',
}

print(phonebook)

phonebookKey = input('Enter a name: ')
phonebookValue = input('Enter a phone number: ')
phonebook[phonebookKey] = phonebookValue

print(phonebook.items())
print(phonebook.keys())
