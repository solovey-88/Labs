import sys
n, n1, n2, n3 = int(input()), 0, 0, 0
n3 = n%10
n2 = (n//10)%10
n1 = n//100
n3_dict = dict([(1, 'один'), (2, 'два'), (3, 'три'), (4, 'четыре'), (5, 'пять'), (6, 'шесть'), (7, 'семь'),
                (8, 'восемь'), (9, 'девять'), (0, '')])
n2_dict = dict([(2, 'двадцать'), (3, 'тридцать'), (4, 'сорок'), (5, 'пятьдесят'), (6, 'шестьдесят'),
                (7, 'семьдесят'), (8, 'восемьдесят'), (9, 'девяносто'), (0, '')])
n1_dict = dict([(1, 'сто'), (2, 'двести'), (3, 'триста'), (4, 'четыреста'), (5, 'пятьсот'), (6, 'шестьсот'),
                (7, 'семьсот'), (8, 'восемьсот'), (9, 'девятьсот'), (0, '')])
if n == 0:
    print('ноль')
    sys.exit()
elif n == 10:
    print('десять')
    sys.exit()
elif n == 11:
    print('одиннадцать')
    sys.exit()
elif n == 12:
    print('двенадцать')
    sys.exit()
elif n == 13:
    print('тринадцать')
    sys.exit()
elif n == 14:
    print('четырнадцать')
    sys.exit()
elif n == 15:
    print('пятнадцать')
    sys.exit()
elif n == 16:
    print('шестнадцать')
    sys.exit()
elif n == 17:
    print('семнадцать')
    sys.exit()
elif n == 18:
    print('восемьнадцать')
    sys.exit()
elif n == 19:
    print('девятнадцать')
    sys.exit()
elif n == 1000:
    print('тысяча')
    sys.exit()
if n1 != 0 and n2 != 0 and n3 != 0:
    print(n1_dict[n1] + ' ' + n2_dict[n2] + ' ' + n3_dict[n3])
elif n1 == 0 and n2 != 0 and n3 != 0:
    print(n2_dict[n2] + ' ' + n3_dict[n3])
else:
    print(n3_dict[n3])