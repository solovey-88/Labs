stroka = input('Введите строку с буквами из латинского алфавита и чисел ')
stroka_list = list(stroka)
summary = len(stroka_list)
final = ''
for i in range(summary-1):
    if stroka_list[i].isnumeric() and stroka_list[i+1].isnumeric():
        new_value = stroka_list[i] + stroka_list[i+1]
        temp = i
        del stroka_list[i]
        del stroka_list[i]
        stroka_list.insert(temp, new_value)
summary = len(stroka_list)
for i in range(summary-1):
    if stroka_list[i].isnumeric() == False and stroka_list[i+1].isnumeric() == True:
        final += stroka_list[i] * int(stroka_list[i+1])
    elif stroka_list[i].isnumeric() == True and stroka_list[i+1].isnumeric() == False:
        final += stroka_list[i+1]
    elif stroka_list[i].isnumeric() == False and stroka_list[i+1].isnumeric() == False:
        final += stroka_list[i+1]
print(final)