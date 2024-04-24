ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
fire = input()
hit = ship.find(fire)
ship = ship.lower()
hit1 = ship.find(fire)
if hit >= 1 or hit1 >= 1:
    print("Вы попали выстрелом")
else:
    print("Вы не попали выстрелом")
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")
print("Ваше имя - {name}, ваша фамилия - {surname}, ваш возраст - {age}".format(name=name, surname=surname, age=age))
print(f"Ваше имя - {name}, ваша фамилия - {surname}, ваш возраст - {age}")
