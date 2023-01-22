budget = float(input())
season = input()

if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        price = budget * 0.30
        print(f'Camp - {price:.2f}')
    elif season == 'winter':
        price = budget * 0.70
        print(f'Hotel - {price:.2f}')
elif budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        price = budget * 0.40
        print(f'Camp - {price:.2f}')
    elif season == 'winter':
        price = budget * 0.80
        print(f'Hotel - {price:.2f}')
elif budget > 1000:
    print(f'Somewhere in Europe')
    if season == 'summer':
        price = budget * 0.90
        print(f'Hotel - {price:.2f}')
    elif season == 'winter':
        price = budget * 0.90
        print(f'Hotel - {price:.2f}')
