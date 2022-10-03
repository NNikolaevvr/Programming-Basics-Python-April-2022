length_in_cm = int(input())
width_in_cm =int(input())
height_in_cm = int(input())
percentage = float(input()) / 100

volume_of_the_tank = length_in_cm * width_in_cm * height_in_cm
volume_in_liters = volume_of_the_tank * 0.001
needed_liters = volume_in_liters * (1 - percentage)

print(needed_liters)