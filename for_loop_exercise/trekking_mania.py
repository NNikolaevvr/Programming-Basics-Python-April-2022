number_of_groups = int(input())
total_people = 0
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
for i in range(0, number_of_groups):
    current_group_of_people = int(input())

    if current_group_of_people <= 5:
        musala += current_group_of_people

    elif 6 <= current_group_of_people <= 12:
        montblanc += current_group_of_people

    elif 13 <= current_group_of_people <= 25:
        kilimanjaro += current_group_of_people

    elif 26 <= current_group_of_people <= 40:
        k2 += current_group_of_people

    else:
        everest += current_group_of_people

total_people = total_climbers = musala + montblanc + kilimanjaro + k2 + everest
percentage_musala = musala / total_climbers * 100
percentage_montblanc = montblanc / total_climbers * 100
percentage_kilimanjaro = kilimanjaro / total_climbers * 100
percentage_k2 = k2 / total_climbers * 100
percentage_everest = everest / total_climbers * 100

print(f'{percentage_musala:.2f}%')
print(f'{percentage_montblanc:.2f}%')
print(f'{percentage_kilimanjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everest:.2f}%')