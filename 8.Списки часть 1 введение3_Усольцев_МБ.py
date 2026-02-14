# Исходные данные
Names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

# Объединение списков в zip-объект
names_and_dogs_names = zip(Names, dogs_names)

# Преобразование zip-объекта в список и вывод
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)