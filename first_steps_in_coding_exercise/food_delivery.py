number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

price_for_chicken_menus = number_of_chicken_menus * 10.35
price_for_fish_menus = number_of_fish_menus * 12.40
price_for_vegetarian_menus = number_of_vegetarian_menus * 8.15

total_price_menus = price_for_fish_menus + price_for_vegetarian_menus + price_for_chicken_menus

price_of_dessert = total_price_menus * 0.20

total_price = total_price_menus + price_of_dessert + 2.50

print(total_price)

