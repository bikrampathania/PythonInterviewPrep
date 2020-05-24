'''
Implementing a double linked list.
'''

class DLLNode(object):

	def __init__(self, value):
		self.value = value
		self.next_node = None
		self.prev_node = None

#Now that we have our node that can reference next and previous values, let's begin to build out our linked list!

a = DLLNode(1)
b = DLLNode(2)
c = DLLNode(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b