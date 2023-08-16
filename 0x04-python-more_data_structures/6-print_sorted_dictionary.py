#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_list = sorted(a_dictionary)
    for ele in my_list:
        print("{:s}: {}".format(ele, a_dictionary[ele]))
