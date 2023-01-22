nylon_square_meters = int(input())
paint_liters = int(input())
diluent_liters = int(input())
hours_needed_for_workers = int(input())

price_for_nylon = (nylon_square_meters + 2) * 1.50
price_for_paint = (paint_liters * 0.10)
price_for_paint = (price_for_paint + paint_liters) * 14.50
price_for_diluent = diluent_liters * 5
sum_of_all_materials = price_for_nylon + price_for_paint + price_for_diluent + 0.40

price_for_workers = (sum_of_all_materials * 0.30) * hours_needed_for_workers
final_price = sum_of_all_materials + price_for_workers

print(final_price)
