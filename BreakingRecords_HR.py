'''
Hacker Rank 'Breaking the Records' problem
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
'''

def breakingRecords(scores):

    highNum = 0
    lowNum = 0
    highScore = lowScore = scores[0]
    i = 1

    while i < len(scores):
        if scores[i] == scores[i - 1]:
            if scores[i] == highScore:
                highScore = scores[i]
            else:
                lowScore = scores[i]
        elif scores[i] > scores[i - 1]:
            if scores[i] > highScore:
                highScore = scores[i]
                highNum += 1
        elif scores[i] < scores[i - 1]:
            if scores[i] < lowScore:
                lowScore = scores[i]
                lowNum += 1
        
        i += 1
    
    return [highNum, lowNum]