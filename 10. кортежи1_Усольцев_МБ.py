# Кортеж с верными ответами
correct_answers = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)

# Список ответов студента
student_answers = [map(int, input().split())]

# Сравнение ответов (преобразуем список в кортеж для сопоставления)
if tuple(student_answers) == correct_answers:
    print("Экзамен сдан")
else:
    print("Экзамен провален")