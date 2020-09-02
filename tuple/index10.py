#Tuple comperhension is not supported by python
#Here we are not getting tuple object and we are gettig generator bject
t=(x**2 for x in range(1,6))
print(type(t))
for x in t:
	print(x)