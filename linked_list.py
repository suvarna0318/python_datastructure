class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
	
class LinkedList:
	def __init__(self):
		self.head=None

	def print_linkedlist(self):

		if self.head is None:
			print("no data")
			return
		cur=self.head
		while cur:
			print(cur.data)
			cur=cur.next

	def append(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
			return
		cur=self.head
		while cur.next:
			cur=cur.next	
		cur.next=new_node
		print('pushed',cur.data)

	def insert_front(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
			return 
		new_node.next=self.head
		self.head=new_node

	# def insert_inbetween(self,p_node,data):
	# 	new_node=Node(data)
	# 	if not p_node:
	# 		print("no previous node")

	# 	cur=self.head
	# 	pre=None
	# 	while cur.data!=p_node:
	# 		pre=cur
	# 		cur=cur.next
	# 	new_node.next=pre.next
	# 	pre.next=cur.next
		
		# new_node.next=p_node.next
		# p_node.next=new_node

	def delete_key(self,key):
		if self.head is None:
			return
		cur=self.head
		if cur.data==key:
			self.head=cur.next
			cur.next=None
			return
		cur=self.head
		pre=None
		while cur.data!=key:
			pre=cur
			cur=cur.next
		pre.next=cur.next
		cur.next=None

	def  length_list(self):
		ind=0
		cur=self.head
		while cur:
			ind+=1
			cur=cur.next
		return ind

llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.insert_front("E")
print(llist.print_linkedlist())
# print(llist.delete_key("E"))
print(llist.print_linkedlist())
print(llist.length_list())
	
