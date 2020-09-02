from sys import argv
print("Arguments with file name")
print(argv)
print("Indexing with file name")
print(argv[0])
print()
for a in argv:
    print(a)
print(type(a))
