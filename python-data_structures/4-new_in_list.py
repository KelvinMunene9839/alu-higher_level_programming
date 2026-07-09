#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return my_list
    new_list = my_list[:]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
