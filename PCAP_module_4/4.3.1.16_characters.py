filename = input('Enter a filename: ')
file = open(filename, 'rt')

output = dict()
for character in file.read():
    # ditch return characters, newline, whitespace etc.
    if character.isalnum(): 
        if character.lower() in output:
            output[character.lower()] += 1
        else: 
            output[character.lower()] = 1

# sort the dictionary by value, descending
output = dict(sorted(output.items(), key=lambda item: item[1], reverse=True))

for key, value in output.items():
    print(f'{key} -> {value}')