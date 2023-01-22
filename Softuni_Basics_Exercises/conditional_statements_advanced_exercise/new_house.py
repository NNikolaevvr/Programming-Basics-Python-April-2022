type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

discount = 0
higher_price = 0

roses = 5 * number_of_flowers
dahlias = 3.80 * number_of_flowers
tulips = 2.80 * number_of_flowers
narcissus = 3 * number_of_flowers
gladiolus = 2.50 * number_of_flowers

total_price = 0

if type_of_flowers == 'Roses':
    total_price = roses
    if number_of_flowers > 80:
        discount = roses * 0.10
        total_price -= discount
elif type_of_flowers == 'Dahlias':
    total_price = dahlias
    if number_of_flowers > 90:
        discount = total_price * 0.15
        total_price -= discount
elif type_of_flowers == 'Tulips':
    total_price = tulips
    if number_of_flowers > 80:
        discount = total_price * 0.15
        total_price -= discount
elif type_of_flowers == 'Narcissus':
    total_price = narcissus
    if number_of_flowers < 120:
        higher_price = total_price * 0.15
        total_price += higher_price
elif type_of_flowers == 'Gladiolus':
    total_price = gladiolus
    if number_of_flowers < 80:
        higher_price = total_price * 0.20
        total_price += higher_price

if budget >= total_price:
    money_left = budget - total_price
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {money_left:.2f} leva left.')
else:
    money_needed = total_price - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')


