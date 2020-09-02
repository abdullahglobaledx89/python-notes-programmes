#TO SORT IN REVERSE OF DEFAULT NATURAL SORTING ORDER:
#We can sort according to reverse of default sorting order by using 
#reverse=True argument

n1=[40,10,30,20]
print("Before sorting list elemnets")
print(n1)
print("After sorting list elements")
n1.sort()
print(n1)
print("Reversing order is if true")
n1.sort(reverse=True)
print(n1)
print("Reversing order is if false")
n1.sort(reverse=False)
print(n1)