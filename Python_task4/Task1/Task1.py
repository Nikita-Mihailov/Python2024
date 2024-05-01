#1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_numbers = [num ** 2 for num in numbers]

print(square_numbers)

#2

weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

days_dict = {index + 1: day for index, day in enumerate(weekdays)}

print(days_dict)

#3

tags = {"python" if tag.lower() == "python" else tag.lower() for tag in
        ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]}
print(tags)
