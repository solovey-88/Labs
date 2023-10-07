n = int(input('Введите число: '))
temp = 0
for i in range(n):
    i+=1
    if i == 1:
        print(i)
        temp = i
    else:
        temp *= 10
        temp += i
        print(temp)

