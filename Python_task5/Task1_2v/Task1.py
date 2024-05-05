import random
import re
import calendar
from datetime import date

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]


def casino(list_el):
    element1 = random.choice(list_el)
    list_el.remove(element1)
    element2 = random.choice(list_el)
    return element1, element2


print(casino(list_el))
calendar_date = str(input("Введите дату формата «ГГГГ-ММ»: "))


def show_calendar(calendar_date):
    pattern = re.compile(r'\d{4}-\d{2}')
    if pattern.match(calendar_date):
        year, month = map(int, calendar_date.split('-'))
        cal = calendar.monthcalendar(year, month)
        for week in cal:
            print(week)
    else:
        print("Неверный формат даты. Пожалуйста, введите дату в формате 'ГГГГ-ММ'.")


show_calendar(calendar_date)
phone_number = str(input("Введите российский номер телефона формата '+7-***-***-**-**': "))


def phone_number_check(phone_number):
    pattern = r'^(\+7|7|8)-\d{3}-\d{3}-\d{2}-\d{2}$'
    if re.match(pattern, phone_number):
        print("Номер телефона {} соответствует формату".format(phone_number))
    else:
        print("Номер телефона {} не соответствует формату".format(phone_number))


phone_number_check(phone_number)
