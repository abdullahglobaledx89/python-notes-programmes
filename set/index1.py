#input values
#set{10,20,30}
#list[40,50,60,10]
s=eval(input("Enter the set:"))
l=eval(input("Enter the list:"))
s.update(l,range(5))
print(s)
print(type(s))