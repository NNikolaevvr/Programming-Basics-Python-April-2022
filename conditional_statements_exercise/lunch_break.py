import math
name_of_tv_show = input()
episode_length = int(input())
time_break = int(input())

time_for_lunch = time_break / 8
time_for_break = time_break / 4

time_left = time_break - time_for_lunch - time_for_break

if time_left >= episode_length:
    minutes_left = time_left - episode_length
    print(f'You have enough time to watch {name_of_tv_show} and left with {math.ceil(minutes_left)} minutes free time.')
else:
    minutes_needed = episode_length - time_left
    print(f"You don't have enough time to watch {name_of_tv_show}, you need {math.ceil(minutes_needed)} more minutes.")