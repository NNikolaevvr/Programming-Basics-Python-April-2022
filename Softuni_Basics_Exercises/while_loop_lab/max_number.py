import sys

current_command = input()

max_num = -sys.maxsize
while current_command != 'Stop':
    number = int(current_command)

    if number > max_num:
        max_num = number

    current_command = input()

print(f'{max_num}')


