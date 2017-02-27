class Node(object):
		'''
		Node Class for SingleLinkedList class
		'''
		def __init__(self, data=0):
			'''
			Constructor for Node Class
			'''
			self.__value = data
			self.__next = None

		def getValue(self):
			'''
			Returns the Value of the Node
			'''
			return self.__value

		def setValue(self, data):
			'''
			Sets the Value of the Node
			'''
			self.__value = data

		def getNext(self):
			'''
			Returns the NextPtr of the Node
			'''
			return self.__next

		def setNext(self, node_obj):
			'''
			Sets the NextPtr of the Node
			'''
			self.__next = node_obj


class Stack(object):
	'''
	Python 2.7 implementation of Single Linked List
	'''
	def __init__(self):
		'''
		Constructor of SingleLinkedList class
		'''
		self.head = None
		self.tail = None
		self.size = 0

	def length(self):
		'''
		Function returns the size of the LinkedList
		'''
		return self.size

	

	def push(self, data):
		'''
		Adds new Node to the end of the Stack
		'''
		if (self.size == 0):
			#If there exists no Nodes in the Stack
			new_node = Node(data)
			self.head = new_node
			self.tail = self.head
		else:
			new_node = Node(data)
			self.tail.setNext(new_node)
			self.tail = new_node
					
		#Increment size of the List
		self.size += 1

	
	
	def pop(self):
		if(self.size == 0):
			print "No elements in the stack"
			return -1
		else:
			#Travel to the tail
			tmp_node = self.head
			while(tmp_node.getNext() != self.tail):
				tmp_node = tmp_node.getNext()
			#Save the previous node to tail
			tail_value = self.tail.getValue()
			del(self.tail)
			self.tail = tmp_node
			#Decrement the size of the list
			self.size -= 1
			return tail_value

	def peek(self):
		if(self.size == 0):
			print "No elements in the stack"
			return -1
		else:
			return self.tail.getValue()

	def printStack(self):
		print "Printing Stack"
		tmp_head = self.head
		if (self.size == 0):
			print "Stack is empty!"
		else:
			tmp_size = self.size
			while (tmp_size > 0):
				print '{} '.format(tmp_head.getValue()),
				tmp_head = tmp_head.getNext()
				tmp_size -= 1
			print ""

def main():
	'''
	Main funciton to test the class
	'''
	mystack = Stack()
	mystack.push(4)
	mystack.push(2)
	mystack.push(-1)
	mystack.printStack()
	print mystack.pop()
	print mystack.peek()

if __name__ == "__main__":
	main()