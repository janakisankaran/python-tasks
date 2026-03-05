# ===== 1. Positive or Negative =====
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# ===== 2. Even or Odd =====
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ===== 3. Largest of Two Numbers =====
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)


# ===== 4. Largest of Three Numbers =====
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# ===== 5. Divisible by 5 and 11 =====
num = int(input("\nEnter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# ===== 6. Leap Year =====
year = int(input("\nEnter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# ===== 7. Vowel or Consonant =====
ch = input("\nEnter a character: ")
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")


# ===== 8. Multiple of 3 and 7 =====
num = int(input("\nEnter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")


# ===== 9. Three-digit Number =====
num = int(input("\nEnter a number: "))
if 100 <= num <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# ===== 10. Greater than 100 =====
num = int(input("\nEnter a number: "))
if num > 100:
    print("Number is greater than 100")
else:
    print("Number is not greater than 100")