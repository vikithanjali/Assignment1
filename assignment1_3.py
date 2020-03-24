def remove(dup):
    fin_list = []
    for n in dup:
        if n not in fin_list:
            fin_list.append(n)
    return fin_list
dup = [2, 4, 10, 20, 5, 2, 20, 4]
print(remove(dup))