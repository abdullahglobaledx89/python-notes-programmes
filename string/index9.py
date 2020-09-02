#Counting substring in the given String
#s.count():-it will search throughout the string
#s.count(substring,begin,end):-it will search from begin index to end-1 index
str1="ababababababbbcccc"
print(str1.count("a"))
print(str1.count("b"))
print(str1.count("c"))
print(str1.count("ab"))
print(str1.count('a',3,7))