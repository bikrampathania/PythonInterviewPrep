'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''

def diagonalDifference(arr, n):

	diag1 = 0
	diag2 = 0

	for i in range(n):
		diag1 = arr[i][i]
		diag2 = arr[i][n - i - 1]

	return abs(diag1 - diag2)
	

'''
n = 3
  
arr = [[11, 2, 4], 
       [4 , 5, 6], 
       [10, 8, -12]] 
  
print(difference(arr, n))

Output: 15
'''