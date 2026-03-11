# Исходные данные
clothes = "домашняя одежда"
meal = "Пиво и чипсы"


# Функция для вывода гардероба
def preferences_of_clothes(cloth):
    print("У меня большой гардероб")
    print(f"Утром лучше всего подходит {cloth}")
    print(f"Днём лучше всего подходит {cloth}")
    print(f"Вечером лучше всего подходит {cloth}")
    print(f"Ночью лучше всего подходит {cloth}")


# Функция для вывода предпочтений в еде
def preferences_of_meals(food):
    print("Мои предпочтения в еде")
    print(f"На завтрак я предпочитаю {food}")
    print(f"На обед я предпочитаю {food}")
    print(f"На ужин я предпочитаю {food}")


# Вызов функций
preferences_of_clothes(clothes)
preferences_of_meals(meal)
