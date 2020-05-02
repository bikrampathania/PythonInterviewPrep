# Implementing Dynamic Array

import ctypes

class DynamicArray(object):
	'''
	Dynamic Array Class (Similar to Python list)
	'''

	def __init__(self):
		self.n = 0 # count actual elements (default is 0)
		self.capacity = 1 # default capacity
		self.A = self.make_array(self.capacity)

	def __len__(self):
		"""
		Return number of elements sorted in an array
		"""
		return self.n

	def __getitem__(self, k):
		"""
		Return element at index k
		"""
		if 0 <= k < self.n:
			return IndexError('K is out of range') # check if k is in bounds of array

		return self.A[k] # Retrieve from array at index k

	def append(self, ele):
		if self.n == self.capacity:
			self._resize(2 * self.capacity) # double the capacity if not enough room

		self.A[self.n] = ele # set self.n index to element
		self.n += 1

	def _resize(self, new_cap):
		"""
		Resize internal array to capacity new_cap
		"""
		B = self.make_array(new_cap) # new bigger array

		for k in range(self.n): # reference all existing values
			B[k] = self.A[k]

		self.A = B # call A new bigger array
		self.capacity = new_cap # reset the capacity to new_cap

	def make_array(self, new_cap):
		"""
		Returns a new array with new capacity new_cap
		"""
		return (new_cap * ctypes.py_object)()


# arr = DynamicArray()
# arr.append(1)
# len(arr)
# ...








