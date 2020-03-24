def fun(my_list):
    new_list = []

    while my_list:
        min = my_list[0]
        for x in my_list:
            if x < min:
                min = x
        new_list.append(min)
        my_list.remove(min)
    max_value = new_list[-1]
    min_value = new_list[0]

    return max_value,min_value;

my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = fun(my_list)
print("max value",new_list[0])
print("min value",new_list[1])
