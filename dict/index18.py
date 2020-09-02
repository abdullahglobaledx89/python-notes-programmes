#setdefault():-if the key is already available then this function returns the coreesponding values
#if the key is not available then the specified key-value will be added as new item to Dictionary
dict={100:'salman khan',200:'srk',300:'amir khan'}
print(dict)
print(dict.setdefault(400,'Saif ali khan'))
print(dict)
print(dict.setdefault(100,'Sachin Tendulkar'))
print(dict)
