from random import randint
listok = [randint(1, 100) for i in range(10)]
print(listok)
maximal, minimal = -10000, 10**7
index_max, index_min = 0, 0
for i in range(len(listok)):
    if listok[i] > maximal:
        maximal = listok[i]
        index_max = i
    if listok[i] < minimal:
        minimal = listok[i]
        index_min = i
print(maximal, minimal)
print(index_max, index_min)
listok_new = listok.copy()
listok_new[index_max], listok_new[index_min] = listok_new[index_min], listok_new[index_max]
print(listok_new)
