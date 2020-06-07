'''
Encapsulate memoized process in a class
'''

class Memoize(object):
	def __init__(self, f):
		self.f = f
		self.memo = {}

	def __call__(self, *args):
		if args not in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

def factorial(k):
	if k < 2:
		return 1

	return k * factorial(k - 1)


factorial = Memoize(factorial)