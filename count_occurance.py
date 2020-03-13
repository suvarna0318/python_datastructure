class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	def print_linkedlist(self):

		if self.head is None:
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
		

	def count_ocuurance(self,key):
		cur=self.head
		pre=None
		count=0
		while cur:
			if cur.data==key:
				count+=1
			cur=cur.next
		return count

llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("A")
llist.append("A")
llist.append("A")
llist.append("A")
print(llist.print_linkedlist())
print(llist.count_ocuurance("A"))

			
