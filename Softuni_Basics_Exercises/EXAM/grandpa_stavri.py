numbers_of_days = int(input())
total_amount_of_alcohol = 0
average_amount_degree = 0
sum_degrees = 0
for i in range(numbers_of_days):
    amount_of_alcohol = float(input())
    degrees_of_alcohol = float(input())

    total_amount_of_alcohol += amount_of_alcohol

    total_sum_degree_per_liter_alcohol = amount_of_alcohol * degrees_of_alcohol
    sum_degrees += total_sum_degree_per_liter_alcohol
    average_amount_degree = sum_degrees / total_amount_of_alcohol

print(f'Liter: {total_amount_of_alcohol:.2f}')
print(f'Degrees: {average_amount_degree:.2f}')

if average_amount_degree < 38:
    print(f'Not good, you should baking!')

elif 38 <= average_amount_degree <= 42:
    print(f'Super!')

elif average_amount_degree > 42:
    print(f'Dilution with distilled water!')
