number = int(input())
even = 0
odd = 0
for i in range(0, number):
    current_number = int(input())

    if i % 2 == 0:
        even += current_number

    else:
        odd += current_number

if even == odd:
        print(f'Yes')
        print(f'Sum = {even}')

else:
        diff = abs(even - odd)
        print('No')
        print(f'Diff = {diff}')