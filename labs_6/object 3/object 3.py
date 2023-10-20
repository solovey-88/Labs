text_file = open('text.txt', 'r', encoding='UTF-8')
text_reader = text_file.read()
print(text_reader)
print(len(text_reader))
listr_1, listr_2, stroka = [], [], ''
for i in range(len(text_reader)):
    if text_reader[i].isspace():
        listr_1.append(stroka)
        stroka = ''
        continue
    if text_reader[i].isdigit() or text_reader[i].isalpha():
        stroka += text_reader[i]
        if i == len(text_reader)-1:
            listr_1.append(stroka)
            stroka = ''
            break
print(listr_1)
print(len(listr_1))
for i in range(len(listr_1)):
    if listr_1[i].isnumeric():
        listr_2.append(listr_1[i])
    if listr_1[i].isdigit() == False and listr_1[i+1].isdigit() == False:
        stroka = listr_1[i] + ' ' + listr_1[i+1]
        listr_2.insert(i, stroka)
        stroka = ''
print(listr_2)
dictionary = dict(zip(listr_2[1:len(listr_2):2], listr_2[0:len(listr_2):2]))
print(dictionary)
maximal, minimal = max(dictionary), min(dictionary)
maximal_file, minimal_file = open('maximal.txt', 'w'), open('minimal.txt', 'w')
text_file.close()