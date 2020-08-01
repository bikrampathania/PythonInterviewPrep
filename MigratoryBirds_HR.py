'''
Solution to Migratory Birds problem on HackerRank
https://www.hackerrank.com/challenges/migratory-birds/problem
'''

def migratoryBirds(arr):
    
    birdPairs = {}
    
    for i in arr:
        if i in birdPairs:
            birdPairs[i] += 1
        else:
            birdPairs[i] = 1
    #print(birdPairs)
    
    maxIter = max(birdPairs.values())
    #print(maxIter)
    
    birdType = [k for k in birdPairs if birdPairs[k] == maxIter]
    #print(birdType)
    return min(birdType)