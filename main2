import string
while(1):
    line = input()
    line = line.split(" ")
    for i in range(len(line)):
        line[i] = line[i].translate(str.maketrans("", "", string.punctuation))
    if "" in line:
        line.remove("")
    dic = {}
    for i in line:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic_key = []
    for i in dic:
        dic_key.append(i)
    pop_list = []
    which_list = []
    for i in range(len(dic_key)):
        for j in range(i+1, len(dic_key)):
            if (dic_key[i].casefold() == dic_key[j].casefold()):
                which_list.append(dic_key[i])
                pop_list.append(dic_key[j])
    for i in range(len(which_list)):
        dic[which_list[i]] += dic[pop_list[i]]
    print(which_list, pop_list)
    for i in pop_list:
        dic.pop(i)
    for i in dic:
        print("{} : {}".format(i, dic[i]))
