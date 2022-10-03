current_command = input()
sum_money = 0
while current_command != 'NoMoreMoney':
    number = float(current_command)

    if number < 0:
        print(f'Invalid operation!')
        break

    print(f'Increase: {number:.2f}')

    sum_money += number

    current_command = input()

print(f'Total: {sum_money:.2f}')

