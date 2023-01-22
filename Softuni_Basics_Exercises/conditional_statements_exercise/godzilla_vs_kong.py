budget = float(input())
number_of_actors = int(input())
price_per_cloth = float(input())

movie_decor = 0.10 * budget

if number_of_actors > 150:

    price_per_cloth -= price_per_cloth * 0.10


price_for_all_clothes = price_per_cloth * number_of_actors
price_for_movie = price_for_all_clothes + movie_decor

final_budget = abs(price_for_movie - budget)


if price_for_all_clothes + movie_decor > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {final_budget:.2f} leva more.')

else:
    print(f'Action!')
    print(f'Wingard starts filming with {final_budget:.2f} leva left.')