fruit = input()
day_of_week = input()
quantity = float(input())
price = 0

if fruit == 'banana':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 2.50
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 2.70
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'apple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 1.20
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 1.25
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'orange':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 0.85
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 0.90
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'grapefruit':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 1.45
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 1.60
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'kiwi':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 2.70
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 3.00
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'pineapple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 5.50
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 5.60
        print(f'{price:.2f}')
    else:
        print('error')
elif fruit == 'grapes':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
        price = quantity * 3.85
        print(f'{price:.2f}')
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 4.20
        print(f'{price:.2f}')
    else:
        print('error')


else:
    print('error')

