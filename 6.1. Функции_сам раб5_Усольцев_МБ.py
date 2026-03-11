# Исходный балл
mark = 4.6


# Функция для преобразования балла в грейд
def mark_to_grade(mark_value):
    if mark_value >= 4.0:
        return "A"
    elif mark_value >= 3.0:
        return "B"
    elif mark_value >= 2.0:
        return "C"
    elif mark_value >= 1.0:
        return "D"
    elif mark_value >= 0.0:
        return "F"


# Вызов функции и вывод результата
grade = mark_to_grade(mark)
print(grade)
