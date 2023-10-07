st_l = list(input())
n_l = []
st_l_no_dupl = []
number = 1
length = len(st_l)
for i in range(length-1):
    if st_l[i] == st_l[i+1]:
        number += 1
    else:
        n_l.append(number)
        number = 1
        st_l_no_dupl.append(st_l[i])
n_l.append(number)
st_l_no_dupl.append(st_l[-1])
dictionary = dict(zip(st_l_no_dupl, n_l))
sorted_dictionary = sorted(dictionary.items(), key = lambda item: item[1], reverse=True)
for i in range(3):
    print(*sorted_dictionary[i])


