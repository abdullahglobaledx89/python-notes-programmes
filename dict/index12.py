#pop():-It removes the entry associated with the specified key and value and returns corresponding value
#if the specified key is not there then we will get key error
dict={1001:100000,1002:200000,1003:300000}
print("before performing pop() function")
print(dict)
print()
print("After performing the pop() function")
print(dict.pop(1001))
print(dict)
print()
print(dict.pop(1004))
