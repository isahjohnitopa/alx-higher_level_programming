def search_replace(my_list, search, replace):
    my_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace

    return my_list
