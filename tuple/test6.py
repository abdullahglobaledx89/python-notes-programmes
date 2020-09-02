t1=eval(input("Enter any tuple:"))
print("Before sorting the items in tuple")
print(t1)
t2=sorted(t1)
print("After sorting the items within the tuple")
print(t2)
print("Fetching the data from the tuple")
for t3 in t2:
	print(t3)
print("Reverse of tuple")
t4=sorted(t1,reverse=True)
print(t4)

