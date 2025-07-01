# example1 : read the content of a file
"""
file = open('chuck_norris.txt', 'r')
content = file.read()
print(content)
file.close()
"""


# example2 : read the content of a file per line using the 'with' statement
with open('chuck_norris.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())