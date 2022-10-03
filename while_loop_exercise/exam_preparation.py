max_poor_grades = int(input())
failed_times = 0
grades_sum = 0
solved_tasks = 0
last_task = ''
while failed_times < max_poor_grades:
    problem_name = input()

    if problem_name == 'Enough':
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1

    grades_sum += grade
    solved_tasks += 1
    last_task = problem_name

if failed_times >= max_poor_grades:
    print(f'You need a break, {failed_times} poor grades.')

else:
    print(f'Average score: {grades_sum / solved_tasks:.2f}')
    print(f'Number of problems: {solved_tasks}')
    print(f'Last problem: {last_task}')