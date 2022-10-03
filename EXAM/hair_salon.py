
target_for_the_day = int(input())
mens = 0
ladies = 0
kids = 0

touch_up = 0
full_color = 0
sum_total = 0

while True:

    services = input()

    if services == 'closed':
        break

    if services == 'haircut':
        type_of_haircut = input()

        if type_of_haircut == 'mens':
            mens += 15

        elif type_of_haircut == 'ladies':
            ladies += 20

        elif type_of_haircut == 'kids':
            kids += 10

    elif services == 'color':
        type_of_color = input()

        if type_of_color == 'touch up':
            touch_up += 20

        elif type_of_color == 'full color':
            full_color += 30

    sum_total = mens + ladies + kids + touch_up + full_color
    if sum_total >= target_for_the_day:
        break

if sum_total < target_for_the_day:
    diff = abs(target_for_the_day - sum_total)

    print(f'Target not reached! You need {diff}lv. more.')

else:

    print(f'You have reached your target for the day!')

print(f'Earned money: {sum_total}lv.')