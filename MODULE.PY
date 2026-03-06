# 1. Use math module (square root, power, factorial)
import math
print("1.", "Square Root:", math.sqrt(16))
print("   Power:", math.pow(2, 3))
print("   Factorial:", math.factorial(5))


# 2. Display all functions in math module
print("2.", dir(math))


# 3. Generate random numbers
import random
print("3.", "Random Number:", random.randint(1, 100))


# 4. Shuffle elements of a list
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print("4.", "Shuffled List:", lst)


# 5. Generate random password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for i in range(8):
    password += random.choice(chars)
print("5.", "Random Password:", password)


# 6. Import user-defined arithmetic module
import arithmetic
print("6.", arithmetic.add(10, 5))
print("   ", arithmetic.subtract(10, 5))
print("   ", arithmetic.multiply(10, 5))
print("   ", arithmetic.divide(10, 5))


# 7. Import student module
import student_module
print("7.")
student_module.display_student()


# 8. Import area module
import area_module
print("8.", "Circle Area:", area_module.circle_area(5))
print("   ", "Square Area:", area_module.square_area(4))
print("   ", "Rectangle Area:", area_module.rectangle_area(5, 3))


# 9. Import user-defined module and call function
print("9.", arithmetic.add(20, 10))


# 10. Use datetime module
import datetime
now = datetime.datetime.now()
print("10.", "Current Date:", now.date())
print("    Current Time:", now.time())
print("    Current Year:", now.year)