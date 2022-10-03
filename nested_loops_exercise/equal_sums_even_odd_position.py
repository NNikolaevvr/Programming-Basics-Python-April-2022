first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):

    sum_odd = 0
    sum_even = 0

    for i in range(len(str(number))):

        if i % 2 == 0:
            sum_even += int(str(number)[i])
        else:
            sum_odd += int(str(number)[i])

    if sum_odd == sum_even:
        print(number, end=' ')


