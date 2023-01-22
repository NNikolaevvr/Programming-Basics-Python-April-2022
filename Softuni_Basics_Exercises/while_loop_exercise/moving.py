width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
free_space = width_free_space * length_free_space * height_free_space
total_space = 0
space_diff = 0
command = input()

while command != 'Done':

    number_of_boxes = int(command)

    total_space += number_of_boxes

    if total_space >= free_space:
        break

    command = input()

if total_space <= free_space:

    print(f'{abs(total_space - free_space)} Cubic meters left.')


else:
    print(f'No more free space! You need {abs(free_space - total_space)} Cubic meters more.')
