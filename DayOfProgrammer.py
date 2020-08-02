'''
Solution to HackerRank's Day of the Programmer problem
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''

def dayOfProgrammer(year):

    if year < 1700 or year > 2700:
        return False

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) or year in (1700,1800,1900):
        return ("12.09." + str(year))
    elif year == 1918:
        return ("26.09." + str(year))
    else:
        return ("13.09." + str(year))