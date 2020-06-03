'''
https://www.hackerrank.com/challenges/apple-and-orange/problem
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):

    numOfApples = 0
    numOfOranges = 0

    applePositionFromTree = []
    orangePositionFromTree = []

    for position in apples:
        applePositionFromTree.append(a + position)
    
    for position in oranges:
        orangePositionFromTree.append(b + position)
    
    for num in applePositionFromTree:
        if s <= num <= t:
            numOfApples += 1
    
    for num in orangePositionFromTree:
        if s <= num <= t:
            numOfOranges += 1
    
    print(numOfApples)
    print(numOfOranges)