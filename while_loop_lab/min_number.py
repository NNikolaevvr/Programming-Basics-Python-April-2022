import sys

current_command = input()

min_num = sys.maxsize
while current_command != 'Stop':
    number = int(current_command)

    if number < min_num:
        min_num = number

    current_command = input()

print(f'{min_num}')


