#!/usr/bin/pythn3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_val = 0
        for ele in my_list:
            if ele > max_val:
                max_val = ele

    return max_val
