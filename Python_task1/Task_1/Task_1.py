while True:
    a = input()
    if a == 'exit':
        break
    try:
        print(len(str(abs(int(a)))))
    except ValueError:
        print('Введите числовое значение')