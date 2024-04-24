x = int(input())
b = 0
c = 0
print('[-число пользователя; число пользователя +1]')
for i in range(-x, x+2):
    print(i, end=' ')
    if i == abs(i):
        b = b + i
    else:
        c = c + i
print()
print('Сумма положительных чисел =', b)
print('Сумма отрицательных чисел =', c)
