'''
HackerLand University has the following grading policy:
- Every student receives a grade in the inclusive range from 0 to 100.
- Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:
- If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
- If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Input:

73
67
38
33

Output:

75
67
40
33
'''

def gradingStudents(grades):

    for grade in grades:
        if grade < 0 or grade > 100:
            return False
    
    finalGrade = []

    for grade in grades:
        if grade < 38:
            finalGrade.append(grade)
        else:
            if (grade + (5 - (grade % 5))) - grade < 3:
                finalGrade.append(grade +(5 - (grade % 5)))
            else:
                finalGrade.append(grade)
    
    return finalGrade
    