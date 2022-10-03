rolls_wrapping_paper = int(input())
fabric_rolls = int(input())
liters_of_glue = float(input())
percentage_discount = int(input())

wrapping_paper = 5.80
fabric = 7.20
glue = 1.20

price_of_wrapping_paper = wrapping_paper * rolls_wrapping_paper
price_of_fabric = fabric * fabric_rolls
price_of_glue = glue * liters_of_glue

total_sum = price_of_wrapping_paper + price_of_fabric + price_of_glue

discount = total_sum * percentage_discount / 100

total_sum -= discount

print(f'{total_sum:.3f}')