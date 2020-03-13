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
		
	def swap(self,k1,k2):
		if k1==k2:
			return 
		pre1=None
		cur1=self.head
		while cur1 and cur1.data!=k1:
			pre1=cur1
			cur1=cur1.next
		print(cur1)

		pre2=None
		cur2=self.head
		while cur2 and cur2.data!=k2:
			pre2=cur2
			cur2=cur2.next
		print(cur2)
		if not cur1 or not cur2:
			return
		if pre1:
			pre1.next=cur2
		else:
			self.head=cur2

		if pre2:
			pre2.next=cur1
		else:
			self.head=cur1



		cur1.next,cur2.next=cur2.next,cur1.next
llist=LinkedList()
llist.append("2")
llist.append("1")
llist.append("4")
llist.append("6")
print(llist.print_linkedlist())
print(llist.swap(1,4))
print(llist.print_linkedlist())





