letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Создание словаря letter_to_points
letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points[""] = 0


#Функция подсчета очков за слово
def score_word (word):
    score = 0
    for letter in word:
        score += letter_to_points.get(letter, 0)
    return score


#Тестирование
print(score_word("BOOK"))

#Словарь игроков и слов
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}


#Функция подсчйта очков игрока
def update_point_totals():
    player_to_points = {}
    for player in player_to_words:
        words = player_to_words[player]
        player_point = 0
        for word in words:
            player_point += score_word(word)
        player_to_points[player] = player_point
    print(player_to_points)


#Функция добавления слова игроком
def play_word (player, word):
    player_to_words[player].append(word.upper())


#Выведим результаты
update_point_totals()