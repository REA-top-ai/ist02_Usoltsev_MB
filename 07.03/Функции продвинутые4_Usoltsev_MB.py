tables = {
 1: {
 'name': 'Chioma',
 'vip_status': False,
 'order': {
 'drinks': 'Orange Juice, Apple Juice',
 'food_items': 'Pancakes'
 }
 },
 2: {},
 3: {},
 4: {},
 5: {},
 6: {},
 7: {},
}


def assign_food_items (**order_items):
    food = order_items.get('food')
    drink = order_items.get('drinks')


assign_food_items(food='Pancakes, Poached Egg', drinks='Water')