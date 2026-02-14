import random

# Создание пустого списка
random_list = []

# Использование list для генерации 101 случайного числа
random_list = [random.randint(1, 100) for i in range(101)]

# Случайный выбор одного элемента из созданного списка
randomer_number = random.choice(random_list)