#input values
#x1={10,20,30,40}
#y1={30,40,50,60}
print("Differnce operation")
x1=eval(input("Enter the set:"))
y1=eval(input("Enter the set:"))
print("One way to perfrom differnce() operation")
print("it takes x1  common items")
print(x1.difference(y1))
print()
print("it takes y1 common items")
print(y1.difference(x1))
print()
print("Another way to perform difference() operation")
print("it take x1 common items")
print(x1-y1)
print("it takes y1 common values")
print(y1-x1)
