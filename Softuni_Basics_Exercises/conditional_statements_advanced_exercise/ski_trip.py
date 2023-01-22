number_of_days = int(input())
type_of_room = input()
feedback = input()
price = 0

if type_of_room == 'room for one person':
    if number_of_days < 10 or 10 <= number_of_days <= 15 or number_of_days > 15:
        price = (number_of_days - 1) * 18

elif type_of_room == 'apartment':
    price = (number_of_days - 1) * 25
    if number_of_days < 10:
        discount = price * 0.30
        price -= discount
    elif 10 <= number_of_days <= 15:
        discount = price * 0.35
        price -= discount
    elif number_of_days > 15:
        discount = price * 0.50
        price -= discount

elif type_of_room == 'president apartment':
    price = (number_of_days - 1) * 35
    if number_of_days < 10:
        discount = price * 0.10
        price -= discount
    elif 10 <= number_of_days <= 15:
        discount = price * 0.15
        price -= discount
    elif number_of_days > 15:
        discount = price * 0.20
        price -= discount

if feedback == 'positive':
    higher_price = price * 0.25
    price += higher_price

elif feedback == 'negative':
    price_discount = price * 0.10
    price -= price_discount

print(f'{price:.2f}')

