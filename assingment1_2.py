def present_key(dic, key,final=[]):
    keys = list(dic.keys())
    if len(keys)==1:
        if key==keys[0]:
            return '->'.join(final)
        elif isinstance(dic[keys[0]], dict):
            final.append(keys[0])
            elements = dic[keys[0]]
            return present_key(elements, key)
        else:
            return "Key not found"

dic = {"a": {"b": {"c": {"d": 1}}}}
key = "b"
result = present_key(dic, key)
print(result)