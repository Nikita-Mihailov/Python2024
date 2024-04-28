def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Делить на 0 нельзя")
    return x / y


def power(x, y):
    return x ** y


def main():
    while True:
        operation = str(input("Введите операцию над числами ('-', '+', '*', '/', '^') или выход ('exit'): "))
        if operation == "exit":
            print("Выход из калькулятора")
            break
        try:
            x = float(input("Введите первое число: "))
            if not isinstance(x, float):
                raise ValueError()
            y = float(input("Введите второе число: "))
            if not isinstance(y, float):
                raise ValueError()
            if operation == "-":
                result = subtraction(x, y)
                print(result)
            elif operation == "+":
                result = addition(x, y)
                print(result)
            elif operation == "*":
                result = multiplication(x, y)
                print(result)
            elif operation == "/":
                result = division(x, y)
                print(result)
            elif operation == "^":
                result = power(x, y)
                print(result)
            else:
                print("Введите операцию из предложенного выбора")
        except ValueError:
            print("Ошибка: введите число")
        except ZeroDivisionError:
            print("Ошибка: на ноль делить нельзя")


main()
