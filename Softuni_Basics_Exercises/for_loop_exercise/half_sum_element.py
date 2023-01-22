import sys

number = int(input())

max_number = -sys.maxsize
total = 0

for num in range(0, number):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    total += current_number

if max_number == total - max_number:
    print('Yes')
    print(f'Sum = {max_number}')

else:
    print('No')
    total -= max_number
    diff = abs(total - max_number)
    print(f'Diff = {diff}')
