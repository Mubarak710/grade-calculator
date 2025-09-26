'''Calculates the total and average scores of your course'''

student_marks = {}

name = input('Enter you name:  ')

subjects = ['English', 'Mathematics', 'Science', 'Computer Science']

for subject in subjects:
    marks = float(input(f'Enter score for {subject}: '))
    student_marks[subject] = marks

print(f'\n Student name = {name}')
print('')

for subject, marks in student_marks.items():
    print(f'{subject}: {marks}')

total = sum(student_marks.values())
average = total / len(subjects)

print('')
print(f'Total score = {total}')
print(f'Average score = {average:.2f}')
print('')
