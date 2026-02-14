import datetime


# 1. Список сотрудников
employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]


# 2. Расчет премии программистам (3%)
def programmer_bonus(employees):
    employees_bonus = []
    for employ in employees:
        if "программист" in employ[1].lower():
            bonus = employ[3] * 0.03
            employees_bonus.append(employ)
            employees_bonus[-1].append(bonus)
    return employees_bonus


# 3. Расчет премии к 8 марта и 23 февраля
def gender_bonus(employees):
    for employ in employees:
        full_name = employ[0]
        # Простая проверка по окончанию отчества для определения пола
        if full_name.split()[2].endswith("на"):
            bonus = 2000  # К 8 марта
        else:
            bonus = 2000  # К 23 февраля


# 4. Индексация зарплат
def index_salaries(employees):
    today = datetime.datetime.now()
    for employ in employees:
        hire_date = datetime.datetime.strptime(employ[2], "%d.%m.%Y")
        years = (today - hire_date).days / 365.25
        if years > 10:
            employ[3] *= 1.07
        else:
            employ[3] *= 1.05
    return employees


# 5. График отпусков (более 6 месяцев работы)
def vacation_list(employees):
    today = datetime.datetime.now()
    vacation_ready = []
    for employ in employees:
        hire_date = datetime.datetime.strptime(employ[2], "%d.%m.%Y")
        months = (today - hire_date).days / 30.44
        if months > 6:
            vacation_ready.append(employ)
    return vacation_ready