# Функция расчета силы
def get_force(m, a):
    """
    m - масса
    a - ускорение
    """
    return m*a


# Функция расчета энергиим
def get_energy(m, c=3 * 10 ** 8):
    """
    m - масса
    c - ускорени, 3 х 10 ^ 8
    """
    return m * c ** 2


# Функция расчета работы через get_force
def get_work(m, a, s):
    """
    m - масса
    a - ускорение
    s - расстояние
    """
    return get_force(m, a) * s


# Данные для тестирования
train_mass = 22680
train_acceleration = 10
train_distance = 100

# Расчет и вывод силы
train_force = get_force(train_mass, train_acceleration)
print(f"Поезд GE поставляет {train_force} ньютонов силы")

# Расчет и вывод энергии для 1 кг
bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print(f"1 кг бомбы составляет {bomb_energy} Джоулей")

# Расчет и вывод работы
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров.")
