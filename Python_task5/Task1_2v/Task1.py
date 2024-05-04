import random

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]


def casino(list_el):
    element1 = random.choice(list_el)
    list_el.remove(element1)
    element2 = random.choice(list_el)
    return element1, element2


print(casino(list_el))
