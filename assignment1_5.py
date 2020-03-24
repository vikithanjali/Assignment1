def validation(fun):
    def wrapper():
        num = fun()
        try:
            val = int(num)
            if isinstance(val,int):
                return "integer"
            else:
                return "value should be integer"
        except:
            return "value should be integer"
    return wrapper

@validation
def fun():
    data = input("enter integer")
    return data
print(fun())
