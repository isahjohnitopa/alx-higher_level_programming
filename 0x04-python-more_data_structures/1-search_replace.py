#!/usr/bin/python3

def search_replace(my_list, search, replace):
    _my_list = my_list[:]
    for i in range(len(_my_list)):
        if _my_list[i] == search:
            _my_list[i] = replace

    return _my_list
