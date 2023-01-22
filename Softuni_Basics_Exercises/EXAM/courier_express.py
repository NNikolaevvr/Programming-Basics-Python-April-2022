shipment_weight_in_kg = float(input())
type_of_service = input()
distance_in_km = int(input())
price_per_km = 0
increase_per_km = 0

if type_of_service == 'standard':
    if shipment_weight_in_kg < 1:
        price_per_km = 0.03

    elif 1 < shipment_weight_in_kg < 10:
        price_per_km = 0.05

    elif 10 <= shipment_weight_in_kg < 40:
        price_per_km = 0.10

    elif 40 <= shipment_weight_in_kg < 90:
        price_per_km = 0.15

    elif 90 <= shipment_weight_in_kg < 150:
        price_per_km = 0.20

    price = distance_in_km * price_per_km

    print(f'The delivery of your shipment with weight of {shipment_weight_in_kg:.3f} kg. would cost {price:.2f} lv.')


elif type_of_service == 'express':
    if shipment_weight_in_kg < 1:
        price_per_km = 0.03
        increase_price = price_per_km * 0.80
        increase_per_km = shipment_weight_in_kg * increase_price

    elif 1 < shipment_weight_in_kg < 10:
        price_per_km = 0.05
        increase_price = price_per_km * 0.40
        increase_per_km = shipment_weight_in_kg * increase_price

    elif 10 <= shipment_weight_in_kg < 40:
        price_per_km = 0.10
        increase_price = price_per_km * 0.05
        increase_per_km = shipment_weight_in_kg * increase_price

    elif 40 <= shipment_weight_in_kg < 90:
        price_per_km = 0.15
        increase_price = price_per_km * 0.02
        increase_per_km = shipment_weight_in_kg * increase_price

    elif 90 <= shipment_weight_in_kg < 150:
        price_per_km = 0.20
        increase_price = price_per_km * 0.01
        increase_per_km = shipment_weight_in_kg * increase_price

    price = distance_in_km * price_per_km

    total_increase = distance_in_km * increase_per_km
    total_sum = price + total_increase

    print(f'The delivery of your shipment with weight of {shipment_weight_in_kg:.3f} kg. would cost {total_sum:.2f} lv.')