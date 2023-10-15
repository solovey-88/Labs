from random import randint
listok_1 = [randint(1, 10) for i in range(10)]
listok_2 = [randint(1, 10) for i in range(10)]
listok_no_dubl = []
count = 0
for i in range(len(listok_1)):
    for j in range(len(listok_2)):
        if listok_2[j] == listok_1[i] and listok_1[i] not in listok_no_dubl:
            listok_no_dubl.append(listok_1[i])
print(listok_1)
print(listok_2)
print(len(listok_no_dubl))