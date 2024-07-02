import random
import string

def password(length, complexity):
    if length < 1:
        return "Hello! , The length of Password should be at least 1"
    
    my_characters = ""
    if complexity == 1:
        my_characters = string.ascii_lowercase
    elif complexity == 2:
        my_characters = string.ascii_letters
    elif complexity == 3:
        my_characters = string.ascii_letters + string.digits
    elif complexity == 4:
        my_characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "complexity level not"

    password = ""
    for i in range(length):
        password += random.choice(my_characters)
    
    return password

# Desired length of the password
length = int(input("Enter the desired length for the password: "))


print("Complexity levels:")
print("1. Low (only lowercase letters)")
print("2. Medium (lowercase and uppercase letters)")
print("3. High (letters and digits)")
print("4. Very High (letters, digits, and special characters)")
complexity_choice = int(input("Enter the complexity level (1-4): "))

# Generate the password
result = password(length, complexity_choice)

print("Generated Password:", result)
