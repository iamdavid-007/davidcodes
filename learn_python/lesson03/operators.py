# 1. Assignment operators "="
name = "Kayode Adebanjo David"
print(name)

#==========================
# 2. Arithmetic operators "+", "-", "*", "/", "+=", "-=", "*=", "/="
answer = 2 + 2
print(answer)
answer = 5 - 2
print(answer)
answer = 5 * 2
print(answer)
answer = 24 / 5
print(answer)
meaning = 25
meaning += 2
print(meaning)
meaning = 25
meaning -= 2
print(meaning)
meaning = 25
meaning *= 2
print(meaning)
meaning = 25
meaning /= 3
print(meaning)
mean = 8.33333
mean = round(mean)
print(mean)

# ................+ can also be used to concatinate
my_name = "Kayode " + "Adebanjo"
print(my_name)

# ..... there is also for division "//" which rounds down the answer of a division operation
answer = 24 // 5
print(answer)

# ..... there is also round function "round(/)" which rounds up the answer of a division operation
answer = round(24 / 5)
print(answer)

# ..... there is also % which gives the remainder of the operation
answer = 24 % 5
print(answer)

# ......there is also exponents "**" 
answer = 20 ** 4
print(answer)

#==========================
# 3 Comaparison Operators
# We have "==", "!=", ">", "<", 

# "==" equals to
name = 50 == 50
print(name)
# "!=" not equals to
name = 50 != 50
print(name)
# ">" greater than
name = 60 > 50
print(name)
# "<" less than
name = 60 < 50
print(name)
# ">=" gtreater than or equals to
name = 60 == 50
print(name)
# "<=" less than or equals to
name = 60 <= 50
print(name)

# Boolean Operators
# The basic boolean values are True and False....... "not"
x = True
y = False
z = True
final_x = not x
print(final_x)
# ....... "and" this checks if both values are true
x = True
y = False
z = True
final_x = x and y
print(final_x)
# ....... "or" this checks if one of the values is true
x = True
y = False
z = True
final_x = x or y
print(final_x)

# Ternary Operator
print('Meaning is greater than 10') if meaning > 10 else print('Meaning is not greater than 10')
