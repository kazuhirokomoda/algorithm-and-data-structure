#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
DP_recursive.py
http://www.itmedia.co.jp/enterprise/articles/1003/06/news002_5.html

Given n, p, q, x and y, return the n-th element of A (index is 0-based).
'''

# initial settings
limit = 10**6
values = dict()

def infinite_sequence(n, p, q, x, y):

    # initial condition
    if n <= 0:
        return 1

    # return value if once stored
    if (n < limit) and (n in values):
        return values[n]

    res = infinite_sequence(n/p - x, p, q, x, y) + infinite_sequence(n/q - y, p, q, x, y)

    # memorize value if n is small enough
    if n < limit:
        values[n] = res

    return res


import time
if __name__=="__main__":

    n=10**13
    p=2
    q=2
    x=0
    y=123456

    start = time.time()
    print infinite_sequence(n, p, q, x, y)

    # time
    elapsed_time = time.time() - start
    print("elapsed_time: {0}".format(elapsed_time))
