annual_tax_for_basketball_training = int(input())

price_basketball_sneakers = annual_tax_for_basketball_training * 0.40
price_basketball_sneakers = annual_tax_for_basketball_training - price_basketball_sneakers
price_basketball_outfit = price_basketball_sneakers * 0.20
price_basketball_outfit = price_basketball_sneakers - price_basketball_outfit
price_basketball_ball = price_basketball_outfit / 4
price_basketball_accessories = price_basketball_ball / 5

total_price = annual_tax_for_basketball_training + price_basketball_sneakers + price_basketball_outfit + \
              price_basketball_ball + price_basketball_accessories

print(total_price)
