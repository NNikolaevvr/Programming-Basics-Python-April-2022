name_of_actor = input()
points_from_academy = float(input())
number_of_jury = int(input())

for i in range(0, number_of_jury):
    current_name = input()
    current_points = float(input())

    total_points = len(current_name) * current_points / 2
    points_from_academy += total_points

    if points_from_academy > 1250.5:
        break

if points_from_academy > 1250.5:

    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {points_from_academy:.1f}!')

else:
    diff = 1250.5 - points_from_academy

    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')