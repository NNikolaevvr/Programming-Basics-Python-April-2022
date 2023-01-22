command = input()
sum_steps = 0
while command != 'Going home':
    steps = int(command)

    sum_steps += steps

    if sum_steps >= 10000:
        break

    command = input()

if command == 'Going home':
    steps_going_home = int(input())
    sum_steps += steps_going_home

if sum_steps >= 10000:

    steps_diff = abs(sum_steps - 10000)
    print(f'Goal reached! Good job!')
    print(f'{steps_diff} steps over the goal!')

else:
    steps_needed = 10000 - sum_steps

    print(f'{steps_needed} more steps to reach goal.')
