cart=[10,20,30,80,50,60]
for item in cart:
    if item>600:
        print("INSURANCE MUST BE REQUIRED")
        break
    print("PROCESSING ITEMS ARE",item)
else:
    print("i will execute if break condtion will false")
print("End of the application")
                  