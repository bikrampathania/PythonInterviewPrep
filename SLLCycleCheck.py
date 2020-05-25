'''
Given a singly linked list, write a function which takes in the
first node in a singly linked list and returns a boolean indicating
if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a
previous node in the list. This is also sometimes known as a circularly linked list.
'''

#SLL node class below:

class SLLNode(object):

	def __init__(self, value)

	self.value = value
	self.next_node = None

# SLL cycle check function below:

def cycle_check(node):

	marker1 = node
	marker2 = node

	while marker2 != None and marker2.next_node != None:
		marker1 = marker1.next_node
		marker2 = marker2.next_node.next_node

		if marker2 == marker1:
			return True

	return False


#Program test below:

from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z # No Cycle Here!


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
