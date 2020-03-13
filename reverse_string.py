from programs import *

def reverse_str(inp):
	s=Stack()
	for i in inp:
		s.push(i)

	rev=""
	while  not s.is_empty():
		rev+=s.pop()

	return rev


print(reverse_str("hello"))

	