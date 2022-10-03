number_packages_food_for_dogs = int(input())
number_packages_food_for_cats = int(input())

food_price_dogs = number_packages_food_for_dogs * 2.50
food_price_cats = number_packages_food_for_cats * 4

total_price = food_price_dogs + food_price_cats

print(f'{total_price} lv.')