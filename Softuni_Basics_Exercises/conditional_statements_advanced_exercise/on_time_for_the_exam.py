hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

total_exam_time = hour_of_exam * 60 + minute_of_exam
arrival_time = hour_of_arrival * 60 + minute_of_arrival

time_diff = abs(total_exam_time - arrival_time)

if arrival_time > total_exam_time:
    print('Late')

    if time_diff >= 60:
        hours_late = time_diff // 60
        minutes_late = time_diff % 60

        print(f'{hours_late}:{minutes_late:02d} hours after the start')

    else:
        print(f'{time_diff} minutes after the start')

elif arrival_time <= total_exam_time and time_diff <= 30:
    print(f'On time')

    if time_diff > 0:
        print(f'{time_diff} minutes before the start')
else:
    print('Early')

    if time_diff >= 60:
        hours_early = time_diff // 60
        minutes_early = time_diff % 60

        print(f'{hours_early}:{minutes_early:02d} hours before the start')
    else:
        print(f'{time_diff} minutes before the start')

