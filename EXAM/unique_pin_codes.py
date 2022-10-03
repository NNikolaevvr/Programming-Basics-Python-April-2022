upper_limit_num1 = int(input())
upper_limit_num2 = int(input())
upper_limit_num3 = int(input())

for num1 in range(2, upper_limit_num1 + 1, 2):
    for num2 in range(2, upper_limit_num2 + 1):
        for num3 in range(2, upper_limit_num3 + 1, 2):
            if num2 != 2 and num2 != 4:
                print(f"{num1} {num2} {num3}")
