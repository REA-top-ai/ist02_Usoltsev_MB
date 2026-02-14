max = 10
min = 5
sr = 7.5 #среднее
standard_deviation = 6

if ((max / sr) > 3 * standard_deviation) or ((sr / min) > 3 * standard_deviation):
    print("В ваших данных имеются выбросы и требуют предобработки")
elif ((max / sr) > 5 * standard_deviation) or ((sr / min) > 5 * standard_deviation):
    print("В ваших данных  имеются экстремальные значения и требуют предобработки")
elif ((max / sr) <= 3 * standard_deviation) or ((sr / min) <= 3 * standard_deviation):
    print("Ваши данные пригодны для анализа")
