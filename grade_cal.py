'''Calculates the total and average scores of your course'''

student_marks = {}


try:
    name = input('Enter you name:  ')
except Exception as e:
    print(f"Error reading name: {e}")
    name = "Unknown"

subjects = ['English', 'Mathematics', 'Science', 'Computer Science']


for subject in subjects:
    while True:
        try:
            marks_input = input(f'Enter score for {subject}: ')
            marks = float(marks_input)
            if marks < 0:
                print("Score cannot be negative. Please enter a valid score.")
                continue
            student_marks[subject] = marks
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"Unexpected error: {e}")

print(f'\n Student name = {name}')
print('')

for subject, marks in student_marks.items():
    print(f'{subject}: {marks}')


try:
    total = sum(student_marks.values())
    average = total / len(subjects) if len(subjects) > 0 else 0
except Exception as e:
    print(f"Error calculating total or average: {e}")
    total = 0
    average = 0

print('')
print(f'Total score = {total}')
print(f'Average score = {average:.2f}')
print('')
