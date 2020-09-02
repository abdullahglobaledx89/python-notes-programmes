#program to display all position of Substring in given main string
s1=input("Enter the main String:")
sub=input("Enter the sub String:")
flag=False
pos=-1
n=len(s1)
while True:
	pos=s1.find(sub,pos+1,n)
	if pos==-1:
		break
	print("Found at position",pos)
	flag=True
if flag==False:
	print("Not found")