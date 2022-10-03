deposit_amount = float(input())
months_deposit = int(input())
annual_interest_rate = float(input()) / 100

month_gain = (deposit_amount * annual_interest_rate) / 12

price = deposit_amount + (months_deposit * month_gain)

print(price)