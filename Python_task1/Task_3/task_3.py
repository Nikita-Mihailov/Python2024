from itertools import permutations
def main():
    number = int(input())
    List = []
    c = -1000
    if number <= c or number >= abs(c):
        print(number, "- четырехзначное число")
        return
    number = str(number)
    for i in number:
        List.append(i)
    if List[0] == List[1] or List[1] == List[2] or List[2] == List[0]:
        print("В числе есть одинаковые цифры")
        return
    permutations_list = list(permutations(List))
    for perm in permutations_list:
        for i in perm:
            print(i, end=" ")
        print()
main()
