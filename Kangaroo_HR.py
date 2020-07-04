'''
https://www.hackerrank.com/challenges/kangaroo/problem
'''

#!/bin/python3

def kangaroo(x1, v1, x2, v2):
    if (x2 > x1 and v2 >= v1) or ((x2 - x1) % (v1 -v2) != 0):
        return 'NO'
    else:
        return 'YES'
