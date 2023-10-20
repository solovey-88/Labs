from random import randint
text_file = open('text.txt', 'w+')
for i in range(10):
    if i == 9:
        text_file.write(str(randint(1, 50)))
    else:
        text_file.write(str(randint(1, 50)) + ' ')
text_file.seek(0)
text_reader = text_file.read()
listr, stroka = [], ''
for i in range(len(text_reader)):
    if text_reader[i].isspace():
        listr.append(int(stroka))
        stroka = ''
        continue
    if text_reader[i].isdigit():
        stroka += text_reader[i]
        if i == len(text_reader)-1:
            listr.append(int(stroka))
            break
output_file = open('output.txt', 'w')
product = 1
for i in range(len(listr)):
    product *= listr[i]
output_file.write(str(product))
output_file.close()
text_file.close()

