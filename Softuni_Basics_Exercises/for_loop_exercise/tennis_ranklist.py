import math

number_of_tournaments = int(input())
initial_points = int(input())
points = 0
won_tournaments = 0
for num in range(0, number_of_tournaments):
    current_placement = input()

    if current_placement == 'W':
        points += 2000
        won_tournaments += 1

    elif current_placement == 'F':
        points += 1200

    elif current_placement == 'SF':
        points += 720

total_points = initial_points + points

average_points = points / number_of_tournaments

percentage_won_tournaments = (won_tournaments / number_of_tournaments) * 100

print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{percentage_won_tournaments:.2f}%')
