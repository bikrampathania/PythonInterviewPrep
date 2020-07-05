'''
Solution to HackerRank's Between Two Sets problem

https://www.hackerrank.com/challenges/between-two-sets/problem
'''

def getTotalX(a, b):
    result = []
    for i in range(min(a), max(b)+1):
        if all(i % anum == 0 for anum in a) and all(bnum % i == 0 for bnum in b):
            result.append(i)
    return len(result)