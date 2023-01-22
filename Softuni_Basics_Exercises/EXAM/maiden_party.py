price_of_maiden_party = float(input())
number_of_love_messages = int(input())
number_of_wax_roses = int(input())
number_of_key_holders = int(input())
number_of_cartoons = int(input())
number_of_presents = int(input())

love_messages = 0.60
wax_rose = 7.20
key_holders = 3.60
cartoons = 18.20
surprise = 22
discount = 0

total_sum = (love_messages * number_of_love_messages) + (number_of_wax_roses * wax_rose) + (number_of_key_holders * key_holders) + (number_of_cartoons * cartoons) + (number_of_presents * surprise)

number_of_articles = number_of_love_messages + number_of_wax_roses + number_of_key_holders + number_of_cartoons + number_of_presents

if number_of_articles > 25:
    discount = total_sum * 0.35

final_price = total_sum - discount

expenses_for_hosting = final_price * 0.10

profit = final_price - expenses_for_hosting

if profit > price_of_maiden_party:
    diff = abs(profit - price_of_maiden_party)

    print(f'Yes! {diff:.2f} lv left.')

else:
    diff = abs(price_of_maiden_party - profit)
    print(f'Not enough money! {diff:.2f} lv needed.')