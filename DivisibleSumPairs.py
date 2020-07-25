'''
Solution to HackerRank's "Divisible Sum Pairs" problem
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
'''

def divisibleSumPairs(n, k, ar):
    pairs = []
    
    for i in range(n):
        for j in range(n):
            if i < j and ((ar[i] + ar[j]) % k == 0):
                pairs.append([ar[i], ar[j]])
    
    return len(pairs)