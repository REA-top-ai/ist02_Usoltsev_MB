# Функция для вычисления возраста
def define_age(current_year, birth_year):
    age = current_year - birth_year
    # Возвращаем результат для дальнейшего использования
    return age


# Сохранение результатов вызова в переменные
my_age = define_age(2049, 1993)
dads_age = define_age(2050, 1953)

# Вывод
print(f"Мне {my_age} лет, а моему отцу {dads_age} лет")
