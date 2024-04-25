input_str = input("Введите строку: ").lower()

char_dict = {}

for char in input_str:
    if char != " ":
        char_dict[char] = char_dict.get(char, 0) + 1

print(char_dict)