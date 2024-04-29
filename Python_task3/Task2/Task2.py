def multiply_elements(elements: list, multiplier=2):
    List = []
    for element in elements:
        element = int(element)
        List.append(element * multiplier)
    return List


multiply_elements_lambda = lambda numbers, multiplier=2: [int(element) * multiplier for element in numbers]


def main():
    global result
    List_elements = []
    elements = str(input("Введите элементы: "))
    multiplier = input("Введите множитель: ")
    for element in elements:
        List_elements.append(element)
    if not multiplier.isdigit():
        result1 = multiply_elements(List_elements)
        result2 = multiply_elements_lambda(List_elements)
    else:
        multiplier = int(multiplier)
        result1 = multiply_elements(List_elements, multiplier)
        result2 = multiply_elements_lambda(List_elements, multiplier)
    print("Вывод через обычную функцию", result1)
    print("Вывод через лямбда функцию", result2)


main()
