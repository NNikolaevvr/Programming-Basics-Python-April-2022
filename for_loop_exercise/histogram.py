number = int(input())

p1_cnt = 0
p2_cnt = 0
p3_cnt = 0
p4_cnt = 0
p5_cnt = 0

for num in range(0, number):
    current_number = int(input())

    if current_number < 200:
        p1_cnt += 1

    elif current_number <= 399:
        p2_cnt += 1

    elif current_number <= 599:
        p3_cnt += 1

    elif current_number <= 799:
        p4_cnt += 1

    else:
        p5_cnt += 1

p1 = (p1_cnt / number) * 100
p2 = (p2_cnt / number) * 100
p3 = (p3_cnt / number) * 100
p4 = (p4_cnt / number) * 100
p5 = (p5_cnt / number) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
