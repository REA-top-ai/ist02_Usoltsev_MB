songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Создание словаря
plays = {song: count for song, count in zip(songs, playcounts)}
print(plays)

# Обновление данных
plays["Purple Haze"] = 1
plays["Respect"] += 5  # Был 89, послушали еще 5 раз

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)