import random


def lottery(user_numbers):
    # Администратор загадывает число от 1 до 9
    admin_number = random.randint(1, 9)
    winners_count = 0

    for num in user_numbers:
        # Считаем сумму цифр числа
        digit_sum = sum(int(digit) for digit in str(num))

        # Проверка условия выигрыша
        if digit_sum % admin_number == 0:
            print(f"Выигрышный номер: {num}")
            winners_count += 1

        # Остановка после 5 победителей
        if winners_count == 5:
            break


# Список номеров от 1 до 100
numbers = list(range(1, 101))
# Перемешаем для случайности
random.shuffle(numbers)
lottery(numbers)