file_path = 'PRG_module_4/myfileOne.txt'

my_file = open(file_path,'r')
file_content =  my_file.readlines()
for line in file_content:
    print(line, end='')

my_file.close()

my_file = open(file_path,'a')
print("#"*120)
print("Write, and press enter to add new text. to quit, write 'q'")
print("#"*120)
while True:
    line = input()
    if line == "q":
        break
    my_file.write(f'{line}\n')

my_file.close()

