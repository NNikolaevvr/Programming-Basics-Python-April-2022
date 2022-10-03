opened_tabs_in_browser = int(input())
salary = int(input())

for num in range(0, opened_tabs_in_browser):
    name_of_website = input()

    if name_of_website == 'Facebook':
        salary -= 150

    elif name_of_website == 'Instagram':
        salary -= 100

    elif name_of_website == 'Reddit':
        salary -= 50

    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:

    print(salary)


