class Node(object):
		'''
		Node Class for Queue class
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


class Queue(object):
	'''
	Python 2.7 implementation of Queue
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
		Adds new Node to the end of the Queue
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
		if (self.size == 0):
			print "Queue is Empty!"
			return -1
		else:
			tmp_node = self.head.getNext()
			tmp_value = self.head.getValue()
			del(self.head)
			self.head = tmp_node
			#Decrement the size of the List
			self.size -= 1
			return tmp_value

	def peek(self):
		if (self.size == 0):
			print "Queue is Empty!"
			return -1
		else:
			return self.head.getValue()

	def printQueue(self):
		print "Printing Queue"
		tmp_head = self.head
		if (self.size == 0):
			print "Queue is empty!"
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
	mystack = Queue()
	mystack.push(4)
	mystack.push(2)
	mystack.push(-1)
	mystack.printQueue()
	print mystack.pop()
	print mystack.peek()

if __name__ == "__main__":
	main()