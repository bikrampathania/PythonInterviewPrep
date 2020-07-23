'''
Solution to HackerRank's Birthday Chocolate problem:
https://www.hackerrank.com/challenges/the-birthday-bar/problem
'''

def birthday(s, d, m):
    i = 0
    pairs = []

    while i < len(s):
        add = 0
        for num in s[i:m+i]:
            add += num
        if add == d:
            pairs.append([s[i:m+i]])
        else:
            add = 0
        i += 1
    return (len(pairs))