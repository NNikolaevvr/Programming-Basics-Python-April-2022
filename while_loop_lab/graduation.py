name = input()
year = 1
fail_count = 0
total = 0

while year <= 12:
    if fail_count > 1:
        break

    grade = float(input())

    if grade < 4:
        fail_count += 1
        continue

    total += grade

    year += 1

if fail_count > 1:
    print(f"{name} has been excluded at {year} grade")

else:
    average_grade = total / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")






