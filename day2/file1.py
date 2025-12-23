print(len("Hello"))

#subscripting
print("Hello"[0])
#strings
print("123"+"456")

#integers = whole numbers
print(123+345)

#large Integers 
print(1234556778)

#float = Floating point numbers 
print(12.34)

#boolian values  =  True or False
print(True)
print(False)

len("Delete")

#type checking
print(type(123))
print(type("hello"))
print(type(123.4))
print(type(True))

#type conversion or type casting
print("Number of letters in your name: " + str(len(input("Enter your name"))))

#basic mathematical operators, +, -, *, /, // and **

#PEMDAS
#Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 + 3 + 3 - 3 - 3)

#better option
print(3 * (3 + 3) / 3 - 3)
bmi = 84 / 1.65 ** 2

print(bmi)
#flooring numbers
print(int(bmi))
# rounding number
print(round(bmi))
print(round(bmi, 3))

#assignment operator
score = 0
score += 1
print(score)
score -= 1
print(score)
score = 2
score *= 2
print(score)
score /= 2
print(score)

#f-string
#In Python, we can use f-strings to insert a variable or an expression into a string.

score  = 0
height = 1.1
is_winning = True

print(f"your height is = {height} and you have scored {score} and your winning is {is_winning}")
