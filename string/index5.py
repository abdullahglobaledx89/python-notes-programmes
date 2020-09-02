#removing spaces from string
#rstrip:-To remove the spaces at right side
#lstrip:-To remove the spaces at left side
#strip:-To remove the spaces both side
city=input("Enter your city name:")
scity=city.strip()
if scity=="Hyderabad":
	print("Famous biryani in the world")
elif scity=="Mumbai":
	print("Bollywood industries")
elif scity=="Rajistan":
	print("Marbles stone are famous")
else:
	print("your city is invalid")