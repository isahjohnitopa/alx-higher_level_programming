#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    max_val = my_list[0]
    for ele in my_list:
        if ele > max_val:
            max_val = ele

    return max_val
