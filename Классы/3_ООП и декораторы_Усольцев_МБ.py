from datetime import datetime
from time import sleep


def is_alive(func):
    def wrapper(self, *args, **kwargs):
        if self.health <= 0:
            print(f'{self.name} мертв и не может действовать!')
            return None
        return func(self, *args, **kwargs)
    return wrapper


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f'[LOG] Начало действия: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'[LOG] Действие завершено')
        return result
    return wrapper


class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.health = 60 if hero_class == 'волшебник' else 100
        self.mana = 50 if hero_class == 'волшебник' else 10
        self.hero_class = hero_class
        self.spell_names = {}
        self.items = {}

    @is_alive
    def attack(self, damage):
        print(f'Герой нанес урон: {damage}')

    @log_action
    def heal(self, amount):
        self.health += amount
        # print(f'Герой восстановил здоровье: {self.health}')

    @is_alive
    def cast_spell(self, spell_name):
        cost = self.spell_names.get(spell_name).get('mana_cost')
        self.mana -= cost
        print(f'Герой использовал заклинание: {spell_name}')

    def add_spell(self, spell_name, mana_cost, attack_damage=None, health_increase=None):
        self.spell_names[spell_name] = {'mana_cost': mana_cost, 'attack_damage': attack_damage, 'health_increase': health_increase}

    def add_item(self, item, parametr, bonus):
        if len(self.items) >= 6:
            print('Нельзя надеть больше 6 предметов')
            return
        self.items[item] = {parametr, bonus}
        if parametr == "health":
            self.health += bonus
        elif parametr == "mana":
            self.mana += bonus
        else:
            print('Данный предмет не может быть экипирован')
            return

    def delete_item(self, item):
        if item in self.items:
            parametr = self.items[item]['parametr']
            bonus = self.items[item]['bonus']
            del self.items[item]

            if parametr == "health":
                self.health -= bonus
            elif parametr == "mana":
                self.mana -= bonus
        else:
            print('Предмет не экипирован')
            return


def easter_event(end_date: datetime):
    def decorator(cls):
        orig_init = cls.__init__

        def new_init(self, name, hero_class):
            orig_init(self, name, hero_class)
            # Сохраняем базовые значения
            self._base_health = self.health
            self._base_mana = self.mana
            # Удаляем оригинальные атрибуты
            del self.health
            del self.mana

            # Добавляем священный посох если ивент активен
            if self._event_active() and "Священный посох" not in self.items:
                bonus = 5 if self.hero_class == 'волшебник' else 0
                self.add_item("Священный посох", "mana", bonus)

        cls.__init__ = new_init

        # Проверка активности ивента
        @classmethod
        def _event_active(cls):
            return datetime.now() < end_date
        cls._event_active = _event_active

        # Свойство health
        @property
        def health(self):
            if self._event_active():
                return self._base_health * 2
            return self._base_health

        @health.setter
        def health(self, value):
            if self._event_active():
                # Лечение/урон применяются к базовому здоровью, делённому на 2
                self._base_health = value / 2
            else:
                self._base_health = value
            if self._base_health < 0:
                self._base_health = 0

        # Свойство mana
        @property
        def mana(self):
            if not self._event_active() and "Священный посох" in self.items:
                self.delate_item("Священный посох")
            if self._event_active():
                base = self._base_mana * 1.5
                return int(base)
            return self._base_mana

        @mana.setter
        def mana(self, value):
            if self._event_active():
                # Обратное преобразование
                self._base_mana = value / 1.5
            else:
                self._base_mana = value
            if self._base_mana < 0:
                self._base_mana = 0

        cls.health = health
        cls.mana = mana
        return cls
    return decorator

easter_end = datetime(2026, 4, 19, 23, 59, 59)
Hero = easter_event(easter_end)(Hero)