month = input()
days = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if days > 14:
        discount = studio * 0.30
        studio -= discount
        discount = apartment * 0.10
        apartment -= discount
    elif days > 7:
        discount = studio * 0.05
        studio -= discount
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if days > 14:
        discount = studio * 0.20
        studio -= discount
        discount = apartment * 0.10
        apartment -= discount

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77

    if days > 14:
        discount = apartment * 0.10
        apartment -= discount
else:

    if days > 14:
        discount = apartment * 0.10
        apartment -= discount

price_studio = days * studio
price_apartment = days * apartment

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')

