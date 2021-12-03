#!/usr/bin/python3
"""
Pascal Triangle Module
"""


def pascal_triangle(n):
    """
    calculate pascal, return list
    """
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        num = 11**i
        li = [int(n) for n in str(num)]
        my_list.append(li)
    return my_list
