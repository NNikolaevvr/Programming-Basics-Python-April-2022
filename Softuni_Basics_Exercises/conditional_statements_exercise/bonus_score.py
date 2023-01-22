number = int(input())
bonus = 0

if number > 1000:
    bonus = 0.10 * number
elif number > 100:
    bonus = 0.20 * number
elif number <= 100:
    bonus = 5

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + number)
