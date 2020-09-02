#formatting the String
name="Jagadeesh"
salary=40000.0
age=22
print("{}'s salary is{} and age is{}".format(name,salary,age))
print("{0}'s salary is{1} and age is{2}".format(name,salary,age))
print("{x}'s salary is{y} and age is{z}".format(z=age,y=salary,x=name))