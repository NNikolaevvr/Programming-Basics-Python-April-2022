import math
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

time = distance_in_meters * time_in_seconds_for_one_meter

slowness = distance_in_meters // 15
slowness = slowness * 12.5

total_time = time + slowness

time_needed_to_beat_the_record = (total_time - record_in_seconds)

if total_time >= record_in_seconds:
    print(f'No, he failed! He was {time_needed_to_beat_the_record:.2f} seconds slower.')

else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')