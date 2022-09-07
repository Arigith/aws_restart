mystring = 'this is a string'
print(mystring)
print(type(mystring))
print(mystring + ' is of the data type ' + str(type(mystring)))

#Working with string concatenation
firststring = 'water'
secondstring = 'fall'
thirdstring = firststring + secondstring
print(thirdstring)

#Working with input strings
name = input('What is your name? ')
print(name)

#Formatting output strings
color = input ('what is your favourite colour? ')
animal  = input ('what is your favourite animale? ')
print(f'{name}, you like a {color} {animal}')