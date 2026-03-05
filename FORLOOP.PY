# ===== 11. Print numbers from 1 to 10 =====
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()


# ===== 12. Even numbers from 1 to 50 =====
print("\nEven numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()


# ===== 13. Odd numbers from 1 to 50 =====
print("\nOdd numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")
print()


# ===== 14. Sum of numbers from 1 to 100 =====
sum = 0
for i in range(1, 101):
    sum += i
print("\nSum from 1 to 100:", sum)


# ===== 15. Multiplication table =====
num = int(input("\nEnter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# ===== 16. Count numbers in a list =====
lst = [10, 20, 30, 40, 50]
count = 0
for i in lst:
    count += 1
print("\nCount of elements in list:", count)


# ===== 17. Print elements in a list =====
lst = [1, 2, 3, 4, 5]
print("\nElements in list:")
for i in lst:
    print(i, end=" ")
print()


# ===== 18. Count vowels in a string =====
string = input("\nEnter a string: ")
vowels = 0
for ch in string.lower():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1
print("Number of vowels:", vowels)


# ===== 19. Reverse numbers from 10 to 1 =====
print("\nNumbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()


# ===== 20. Factorial of a number =====
num = int(input("\nEnter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial is:", fact)


# ===== 21. Largest number in a list =====
lst = [12, 45, 7, 89, 23]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print("\nLargest number in list:", largest)


# ===== 22. Count digits in a number =====
num = int(input("\nEnter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits:", count)


# ===== 23. Square of numbers from 1 to 10 =====
print("\nSquares from 1 to 10:")
for i in range(1, 11):
    print(i*i, end=" ")
print()


# ===== 24. Cube of numbers from 1 to 10 =====
print("\nCubes from 1 to 10:")
for i in range(1, 11):
    print(i*i*i, end=" ")
print()


# ===== 25. Sum of elements in a list =====
lst = [5, 10, 15, 20, 25]
total = 0
for i in lst:
    total += i
print("\nSum of list elements:", total)