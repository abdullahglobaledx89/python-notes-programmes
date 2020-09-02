#index():-it is same as find method but if there no string it returns value error
#rfind():-for negative index
#rindex():-for negative index
s1=input("Enter the main String:")
sub=input("Enter the sub string:")
try:
	n=s1.index(sub)
except ValueError:
	print("substring not found")
else:
	print("substring found")
