#!/usr/bin/python3


def uniq_add(my_list=[]):
    my_set = set(my_list)
    reslt = 0
    for ele in my_set:
        reslt += ele
    return reslt
