from matplotlib import pyplot as plt
import random

# Создание диапазона чисел от 1 до 12 включительно
number_a = range(1, 13)

# Создание случайной выборки из 12 чисел в диапазоне (1000)
number_b = random.sample(range(1000), 12)

# Построение графика
plt.plot(number_a, number_b)

# Отображение графика
plt.show()