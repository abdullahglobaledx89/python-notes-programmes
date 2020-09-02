#To check Type of characters present in a string
#isalnum():Returns True if all characters are alphanumeric(atoz AtoZ 0to9)
#isalpha():Returns True if all characters are only alphabet symbols(a to z AtoZ)
#isdigit():Returns True if all characters are only digit(0to9)
#islower():Returns True if all characters are in lowercase only
#isupper():Returns True if all character are in uppercase
#istitle():Returns True if string in title case
#isspace():Returns True if the string contains only spaces

print('GlobalEDX2011'.isalnum())
print('globalEDX2011'.isalpha())
print('globalEDX'.isalpha())
print('globalEDX'.isdigit())
print('20112019'.isdigit())
print('abc'.islower())
print('Abc'.islower())
print('abc123'.islower())
print('ABC'.isupper())
print('Learning Python Is Very Easy'.istitle())
print('learning python Is very easy'.istitle())
print("".isspace())
print(" ".isspace())