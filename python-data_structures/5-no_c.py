#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return my_string
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
