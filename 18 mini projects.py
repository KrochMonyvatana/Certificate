#Exercise 1: Hello Python
# Print a greeting message
print("Hello, Python!")


#Exercise 2: Variable Types
# Create variables of different types and print them
age = 25           # int
height = 5.9       # float
name = "Alice"     # str
is_student = True  # bool
print(age, height, name, is_student)

#Exercise 3: Simple Math
# Use arithmetic operators
a = 10
b = 3
print("Addition:", a + b)
print("Division:", a / b)
print("Power:", a ** b)


#Exercise 4: Compare Numbers
x = 7
y = 5
print("x > y:", x > y)
print("x == y:", x == y)
print("x != y:", x != y)


#Exercise 5: Positive or Negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


#Exercise 6: Print Even Numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(i)



#Exercise 7: Add Two Numbers
def add(a, b):
    return a + b

print(add(5, 7))


#Exercise 8: Greet User
def greet(name):
    return f"Hello, {name}!"

user_name = input("Enter your name: ")
print(greet(user_name))


#Exercise 9: List Operations
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
for fruit in fruits:
    print(fruit)


#Exercise 10: Dictionary Example
student = {"name": "John", "age": 20}
student["grade"] = "A"
print(student)


#Exercise 11: Simple Input
name = input("Enter your name: ")
print(f"Hello, {name}!")


#Exercise 12: Sum Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum: {num1 + num2}")


#Exercise 13: Write to File
with open("example.txt", "w") as f:
    f.write("Hello, file!")


#Exercise 14: Read from File
with open("example.txt", "r") as f:
    content = f.read()
print(content)


#Exercise 15: Handle Invalid Number
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")


#Exercise 16: Division with Error Handling
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")



#Exercise 17: Math Library
import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)


#Exercise 18: List Files with OS
import os
files = os.listdir(".")
print("Files in current directory:", files)
