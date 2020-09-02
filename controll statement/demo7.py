x1=eval(input("Enter the number of x1:"))
x2=eval(input("Enter the number of x2:"))
x3=eval(input("Enter the number of x3:"))
if x1>x2 and x1>x3:
    print("Largest number is",x1)
elif x2>x3:
    print("Largest number is",x2)
else:
    print("Largest number is",x3)
