#List Comrehensions
#it is very easy and compact way of creating list object from any iterable objects 
#(like list,Tuple,Dictonary,Range etc)based on reqn
l=[x*x for x in range(1,11)]
print(l)
for s1 in l:
	print(s1)
l1=[2**x for x in range(1,6)]
print(l1)
for s2 in l1:
	print(s2)

l2=[x for x in l if x%2==0]
print(l2)
for s3 in l2:
	print(s3)