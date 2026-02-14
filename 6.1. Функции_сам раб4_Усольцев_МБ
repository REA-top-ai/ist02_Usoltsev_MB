user_name = ""
# Переменные с сообщениями
dmitriy_check = ("Дмитрий, твое рабочее место находится в другой комнате. "
                 "Отойди от чужого компьютера и займись работой!")
greeting = "Добро пожаловать!"


# Функция для проверки доступа (Задача 4)
def check_access_complete(user_name, arm):
    # Соответствие АРМ
    if user_name == "Дмитрий" and arm == 1:
        print(greeting)
    elif user_name == "Ангелина" and arm == 2:
        print(greeting)
    elif user_name == "Василий" and arm == 3:
        print(greeting)
    elif user_name == "Екатерина" and arm == 4:
        print(greeting)
    # Проверка для Дмитрия на чужом месте
    elif user_name == "Дмитрий":
        print(dmitriy_check)
    else:
        print("Логин или пароль не верный, попробуйте еще раз")


# Проверка для задания 5 (вывод для двух имен)
user_name = "Дмитрий"
if user_name == "Дмитрий":
    print(dmitriy_check)
else:
    print(greeting)

user_name = "Ангелина"
if user_name == "Дмитрий":
    print(dmitriy_check)
else:
    print(greeting)

# Вызов комплексной проверки
check_access_complete("Дмитрий", 1)
