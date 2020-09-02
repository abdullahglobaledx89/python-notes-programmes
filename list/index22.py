#USING MATHEMATICAL OPERATORS FOR LIST OBJECTS
#note:-to use '+' operator compulsory both argument should be list only
print("Byusing plus operator +")
a=[10,20,30,40]
b=[50,60,70,80]
c=a+b
print(c)
print()
print("Bying repetition operator *")
x=[10,20,30]
y=x*3
print(y)
print(type(y))
print()
print("Byusing Equality operators")
x=["Dog","Cat","Rat"]
y=["Dog","Cat","Rat"]
z=["Dog","Cat","RAT"]
print(x==y)
print(x==z)
print(x!=z)

#whenever we are using relational operators(<,<=,>,>=)between list object than only 1st element comparision will be performed
print("Byusing comparision operator < > <= >=")
x=[50,40]
y=[40,20,45,60]
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

print()
print("Byusing comarision operators with string as element in list")
a=["Dog","Cat","Rat"]
b=["Rat","Cat","Dog"]
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
