budget = float(input())
number_of_gpus = int(input())
number_of_cpus = int(input())
number_of_rams = int(input())

price_for_gpus = number_of_gpus * 250
price_for_cpus = 0.35 * price_for_gpus
final_price_for_cpus = price_for_cpus * number_of_cpus

price_for_rams = 0.10 * price_for_gpus
final_price_for_rams = price_for_rams * number_of_rams

total_price = final_price_for_cpus + final_price_for_rams + price_for_gpus

if number_of_gpus > number_of_cpus:
    total_price -= total_price * 0.15


if budget >= total_price:
    money_left = budget - total_price
    print(f'You have {money_left:.2f} leva left!')
else:
    money_left = total_price - budget
    print(f'Not enough money! You need {money_left:.2f} leva more!')
