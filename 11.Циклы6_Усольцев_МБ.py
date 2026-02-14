single_digits = list(range(10))
squares = []

# Цикл для вычисления квадратов
for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)

print(squares)

# Генератор списка для вычисления кубов
cubes = [digit ** 3 for digit in single_digits]
print(cubes)