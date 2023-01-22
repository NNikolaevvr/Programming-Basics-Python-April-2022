starting_number = int(input())
ending_number = int(input())
magic_num = int(input())

flag = False
count = 0
for i in range(starting_number, ending_number + 1):
    for j in range(starting_number, ending_number + 1):
        sum_num = i + j
        count += 1

        if sum_num == magic_num:
            print(f"Combination N:{count} ({i} + {j} = {sum_num})")
            flag = True
            break

    if flag:
        break

if not flag:
    print(f"{count} combinations - neither equals {magic_num}")

