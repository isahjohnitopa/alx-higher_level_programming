#!/usr/bin/pythn3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_val = 0
        for j in range(len(my_list)):
            if my_list[j] > max_val:
                max_val = my_list[j]

    return max_val
