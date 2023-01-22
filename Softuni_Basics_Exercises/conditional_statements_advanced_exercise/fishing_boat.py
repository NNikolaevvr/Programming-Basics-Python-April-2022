budget_of_group = int(input())
season = input()
number_of_fishermen = int(input())
rent_for_ship = 0

if season == 'Spring':
    rent_for_ship = 3000
    if number_of_fishermen <= 6:
        discount = rent_for_ship * 0.10
        rent_for_ship -= discount
    elif 7 <= number_of_fishermen <= 11:
        discount = rent_for_ship * 0.15
        rent_for_ship -= discount
    elif number_of_fishermen >= 12:
        discount = rent_for_ship * 0.25
        rent_for_ship -= discount

elif season == 'Summer' or season == 'Autumn':
    rent_for_ship = 4200
    if number_of_fishermen <= 6:
        discount = rent_for_ship * 0.10
        rent_for_ship -= discount
    elif 7 <= number_of_fishermen <= 11:
        discount = rent_for_ship * 0.15
        rent_for_ship -= discount
    elif number_of_fishermen >= 12:
        discount = rent_for_ship * 0.25
        rent_for_ship -= discount
elif season == 'Winter':
    rent_for_ship = 2600
    if number_of_fishermen <= 6:
        discount = rent_for_ship * 0.10
        rent_for_ship -= discount
    elif 7 <= number_of_fishermen <= 11:
        discount = rent_for_ship * 0.15
        rent_for_ship -= discount
    elif number_of_fishermen >= 12:
        discount = rent_for_ship * 0.25
        rent_for_ship -= discount

if number_of_fishermen % 2 == 0 and season != 'Autumn':
    discount = rent_for_ship * 0.05
    rent_for_ship -= discount

if budget_of_group >= rent_for_ship:
    money_left = budget_of_group - rent_for_ship
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = rent_for_ship - budget_of_group
    print(f'Not enough money! You need {money_needed:.2f} leva.')
