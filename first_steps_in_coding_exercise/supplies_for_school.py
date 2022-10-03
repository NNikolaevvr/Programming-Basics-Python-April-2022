number_of_pen_packages = int(input())
number_of_marker_packages = int(input())
liters_cleaning_agent = int(input())
discount = int(input()) / 100

price_pen_packages = number_of_pen_packages * 5.80
price_marker_packages = number_of_marker_packages * 7.20
price_cleaning_agent = liters_cleaning_agent * 1.20

price_for_all_materials = price_pen_packages + price_marker_packages + price_cleaning_agent
price_for_all_materials -= (price_for_all_materials * discount)

print(price_for_all_materials)

