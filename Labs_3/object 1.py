stroka = input('Введите строку из букв латинского алфавита')
stroka_list = list(stroka)
duplicate = []
for item in stroka_list:
    if stroka_list.count(item) > 1 and item not in duplicate:
        duplicate.append(item)
        numbers = stroka_list.count(item)
        duplicate.append(numbers)
    elif stroka_list.count(item) == 1:
        duplicate.append(item)
print(''.join(map(str, duplicate)))