#Write a python program to add all elements list upto 100 which are divisible by 10
list=[]
for i in range(101):
	if i%2==0:
		list.append(i)
print(list)
for l2 in list:
	print(l2)