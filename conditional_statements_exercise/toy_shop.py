price_for_tour = float(input())
number_of_puzzle = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_price = number_of_puzzle * 2.60 + number_of_dolls * 3 + number_of_teddy_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks * 2
number_of_toys = number_of_puzzle + number_of_dolls + number_of_teddy_bears + number_of_minions + number_of_trucks

if number_of_toys >= 50:
   total_price -= total_price * 0.25


rent = total_price * 0.10
rent = total_price - rent
money_left = abs(rent - price_for_tour)

if rent >= price_for_tour:
    print(f'Yes! {money_left:.2f} lv left.')
else:
  print(f'Not enough money! {money_left:.2f} lv needed.')