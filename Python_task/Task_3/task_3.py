a = int(input())
b = []
c = -1000
if a <= c or a >= abs(c):
    print(a, "- четырехзначное число")
a = str(a)
for i in a:
    b.append(i)
if b[0] == "-":
    b[0] + b[1]
if b[0] == b[1] or b[1] == b[2] or b[2] == b[0]:
    print("в числе есть одинаковые цифры")
print(b[0], b[1], b[2])
print(b[0], b[2], b[1])
print(b[1], b[0], b[2])
print(b[1], b[2], b[0])
print(b[2], b[1], b[0])
print(b[2], b[0], b[1])
