import string
line = input()
line = line.split(" ")
for i in range(len(line)):
    line[i] = line[i].translate(str.maketrans("", "", string.punctuation))
if "" in line:
    line.remove("")
dic = {}
word = []
for i in line:
    q = i.lower()
    if q in dic:
        dic[q] += 1
    else:
        word.append(i)
        dic[q] = 1
for i in range(len(word)):
    print("{} : {}".format(word[i], dic[word[i].lower()]))
