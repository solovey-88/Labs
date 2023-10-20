from random import randint
listr_1, listr_2 = [1, 2, 3, 2, 1], []
for i in range(len(listr_1)):
    if listr_1[i] not in listr_2:
        listr_2.append(listr_1[i])
print(len(listr_2))
print(listr_1)