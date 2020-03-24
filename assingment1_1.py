def func(dic):

    names = set(dic.values())
    d = {}
    for n in names:
        d[n] = [k for k in dic.keys() if dic[k] == n]

    return d;
dic = {"apple": "fruit", "banna": "fruit", "carrot": "vegtable"}
d = func(dic)
print(d)