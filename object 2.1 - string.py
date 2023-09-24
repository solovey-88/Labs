n = int(input('Введите число: '))
for i in range(1, n+1):
    pyramid = ''
    for j in range(1, i+1):
        pyramid += str(j)
    print(pyramid)