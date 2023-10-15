from random import randint
listok = [randint(1, 100) for i in range(10)]
listok_new = []
for i in range(1, len(listok)):
    if listok[i] > listok[i-1]:
        listok_new.append(listok[i])
print(listok)
print(listok_new)
