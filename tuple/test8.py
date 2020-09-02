print("Tuple packing and unpacking process")
a=10
b=20
c=30
d=40
e=50
t=a,b,c,d,e
print(t)
print(type(t))
print("Fetching the data after packing")
for t1 in t:
	print(t1)

print("Hetrogenous data")
Emp_id=1001
Emp_name="Jeff Bezos"
Emp_desig="MD"
Emp_sal=10000000000000000000
t3=Emp_id,Emp_name,Emp_desig,Emp_sal
print(t3)
print("After packing fetching items from tuple")
for t4 in t3:
	print(t4)