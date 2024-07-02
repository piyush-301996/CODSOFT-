# Task - Simple calculator

def add(num_1, num_2):
	return num_1 + num_2

def subtract(num_1, num_2):
	return num_1 - num_2

def multiply(num_1, num_2):
	return num_1 * num_2


def divide(num_1, num_2):
	return num_1 / num_2



# Getting input from user
result = int(input("press No.1 for addition, No. 2 for subtraction, No. 3 for multiplication, No. 4 for division :"))

a = int(input("Enter Your first number:- "))
b = int(input("Enter Your second number:- "))

if result == 1:
	print(a, "+", b, "=", add(a, b))

elif result == 2:
	print(a, "-", b, "=",subtract(a, b))

elif result == 3:
	print(a, "*", b, "=",multiply(a, b))

elif result == 4:
	print(a, "/", b, "=",divide(a, b))
else:
	print("Invalid input")
