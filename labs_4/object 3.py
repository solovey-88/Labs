dictionary = {}
words = []
string = input().split()
for i in range(len(string)):
    if string[i] in dictionary:
        dictionary[string[i]] += 1
    else:
        dictionary[string[i]] = 1
    if string[i] not in words:
        words.append(string[i])
for i in range(len(words)):
    print(dictionary.get(words[i]), end=' ')