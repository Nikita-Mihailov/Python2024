List = []
quantity = int(input("Введите кол-во цифр: "))
print('Введите числа')
for i in range(0, quantity):
        List.append(input())
        List[i] = int(List[i])
level = int(input('Введите степень: '))
for i in range(0, len(List)):
        print(List[i]**level, end=" ")



