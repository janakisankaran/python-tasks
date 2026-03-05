# 1. Add two numbers
def add():
    a = int(input("Enter first number for Addition: "))
    b = int(input("Enter second number: "))
    print("Addition:", a + b)

add()


# 2. Subtract two numbers
def subtract():
    a = int(input("Enter first number for Subtraction: "))
    b = int(input("Enter second number: "))
    print("Subtraction:", a - b)

subtract()


# 3. Multiply two numbers
def multiply():
    a = int(input("Enter first number for Multiplication: "))
    b = int(input("Enter second number: "))
    print("Multiplication:", a * b)

multiply()


# 4. Divide two numbers
def divide():
    a = int(input("Enter first number for Division: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Division by zero not allowed")
    else:
        print("Division:", a / b)

divide()


# 5. Square of a number
def square():
    n = int(input("Enter number to find Square: "))
    print("Square:", n * n)

square()


# 6. Check Even or Odd
def check_even_odd():
    n = int(input("Enter number to check Even/Odd: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd()


# 7. Largest of two numbers
def largest():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b:
        print("Largest:", a)
    else:
        print("Largest:", b)

largest()


# 8. Count vowels in string
def count_vowels():
    text = input("Enter string to count vowels: ")
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print("Vowel Count:", count)

count_vowels()


# 9. Reverse a string
def reverse_string():
    text = input("Enter string to reverse: ")
    print("Reversed String:", text[::-1])

reverse_string()


# 10. Factorial
def factorial():
    n = int(input("Enter number to find Factorial: "))
    if n < 0:
        print("Factorial not defined")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial:", fact)

factorial()


# 11. Sum of list elements
def sum_list():
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    total = 0
    for num in lst:
        total += num
    print("Sum of List:", total)

sum_list()


# 12. Maximum in list
def max_list():
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    print("Maximum:", maximum)

max_list()


# 13. Prime number check
def is_prime():
    n = int(input("Enter number to check Prime: "))
    if n <= 1:
        print("Not Prime")
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")

is_prime()


# 14. Count characters in string
def count_characters():
    text = input("Enter string to count characters: ")
    print("Character Count:", len(text))

count_characters()


# 15. Multiplication table
def multiplication_table():
    n = int(input("Enter number for Multiplication Table: "))
    print("Multiplication Table:")
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

multiplication_table()