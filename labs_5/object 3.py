import sys
n, listr = int(input()), []
for i in range(n):
    city = input()
    if i >= 1:
        if city in listr:
            print('REPEAT')
            sys.exit()
    listr.append(city)
print('OK')
