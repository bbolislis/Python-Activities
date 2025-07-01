# writing to a file
with open('hello.txt', 'w') as file:
    file.write('hello, world!\n')


# append
with open('hello.txt', 'a') as file:
    file.write('greetings from outer space\n')


# write or append multiple lines
additional_lines = ['hello, hooman\n', 'woof-woof']
with open('greetings.txt', 'w'):
    file.writelines(additional_lines)