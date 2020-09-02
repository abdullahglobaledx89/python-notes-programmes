#Aliasing of list object
#The process of giving another refernce variable to the existing list is called aliasing
x=[10,20,30,40]
y=x
print(id(x))
print(id(y))
print()
print()
x1=[10,20,30,40]
y1=x1
y1[1]=777
print(x1)
print(id(x1))
print(id(y1))