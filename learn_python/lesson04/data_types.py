# String data types
import math
# literal assignment of values
first = 'Kayode'
last = 'Adebanjo'

# print(type(first))
# print(type(first) != str)
# print(isinstance(first, str))

# constructor function

# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = "I love music from the " + decade + "s" 
print(statement)

# Multiple lines
multiline = """
Hello babe, how was your day?

I was just checking to see if you are well.
                                                All good?

"""
print(multiline)

# Escaping special characters \   \t = tab   \n = new line
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                       "
multiline = "                   " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Strin index values
print(first[0])
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])
print(first[1:-0])

# Some methods that return boolean data
print(first.startswith("K"))
print(first.endswith("g"))

# Boolean Datatypes

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print("")
# Numerix Datatypes

# 1 integers type [just normal number]
price = 100
last_price = int(80)
print(type(last_price))
print(isinstance(price, int))
print("")

# 2 float type [has decimals]
gpa = 3.72
second_gpa = float(3.45)
print(type(gpa))
print(isinstance(second_gpa, float))
print("")

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print("")

# Built in functions for numbers

print(abs(gpa))
print(abs(second_gpa * -2))

print(round(gpa))

print(round(gpa, 1))
print("")

print(math.pi)
print(math.sqrt(48))
print(math.ceil(gpa))
print(math.floor(second_gpa))
print("")

# casting a string to a number
zipcode = "37005"
zip_value = int(zipcode)
print(type(zip_value))
print("")

# you will get an error if you attempt to cast incorrect data
# zip_value = int("georgia")
# print(type(zip_value))
# the above will return the following error;    invalid literal for int() with base 10: 'georgia'

