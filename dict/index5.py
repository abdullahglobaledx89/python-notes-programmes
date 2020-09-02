#Write a python program to Enter name and percentagemarks by using dictionary and display the informations
record={}
n=eval(input("Enter the number of students:"))
i=1
while i<=n:
	name=input("Enter the name of student:")
	marks=input("Enter the % of marks of student:")
	record[name]=marks
	i=i+1
	print("Name of the Student","\t","% of marks")
	for x in record:
		print("\t",x,"\t\t",record[x])