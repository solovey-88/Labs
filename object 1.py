a, b, c = map(int, input("Введите 3 числа через пробел: ").split())
count = 0
if a == b:
    count += 1
else:
    count += 0
if a == c:
    count += 1
else:
    count += 0
if b == c:
    count += 1
else:
    count += 0
if count == 3:
    print(3)
elif count == 1:
    print(2)
elif count == 0:
    print(0)