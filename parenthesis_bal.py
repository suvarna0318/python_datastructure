from programs import *
#"({})"

def match(t,i):
	print("loop enters")
	if t=='[' and i==']':
		return True
	elif t=='{' and i=='}':
		return True
	elif t=='(' and i==')':
		return True
	else:
		return False
def parenthesis_bal(p_str):
	s=Stack()
	is_bal=True
	ind=0
	while ind<len(p_str) and is_bal:
		paren=p_str[ind]
		if paren in "[{(":
			s.push(paren)
			
		else:
			if s.is_empty():
				is_bal=False
			else:
				top=s.pop()
				if not match(top,paren):
					print(top)
					print(paren)
					print("match checking")
					is_bal=False
		ind+=1
	if s.is_empty() and is_bal:
		print("balanced")
	else:
		print("not balanced")
		
	
		
print(parenthesis_bal("{({{}}())[]}"))





