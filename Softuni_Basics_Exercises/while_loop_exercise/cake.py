length = int(input())
width = int(input())

pieces_left = length * width

command = input()
while command != 'STOP':
    pieces_taken = int(command)
    pieces_left -= pieces_taken



    if pieces_left < 0:
        break

    command = input()
    
if command == 'STOP':
    print(f'{pieces_left} pieces are left.')

else:

    print(f'No more cake left! You need {abs(pieces_left)} pieces more.')

