# 1. Create dictionary with student details
student = {"name": "Ravi", "age": 20, "course": "BSc"}
print("1.", student)

# 2. Access dictionary values using keys
print("2.", student["name"], student["age"])

# 3. Add new key-value pair
student["grade"] = "A"
print("3.", student)

# 4. Update value in dictionary
student["age"] = 21
print("4.", student)

# 5. Delete key from dictionary
del student["course"]
print("5.", student)

# 6. Print all keys
print("6. Keys:")
for key in student.keys():
    print(key)

# 7. Print all values
print("7. Values:")
for value in student.values():
    print(value)

# 8. Print key-value pairs
print("8. Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# 9. Check whether key exists
print("9.", "name" in student)

# 10. Count number of items
print("10. Number of items:", len(student))

# 11. Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print("11.", d1)

# 12. Create dictionary from two lists
keys = ["x", "y", "z"]
values = [10, 20, 30]
d3 = dict(zip(keys, values))
print("12.", d3)

# 13. Sort dictionary by keys
print("13. Sorted by Keys:")
for key in sorted(d3):
    print(key, ":", d3[key])

# 14. Sort dictionary by values
print("14. Sorted by Values:")
for key in sorted(d3, key=d3.get):
    print(key, ":", d3[key])

# 15. Find maximum value
print("15. Maximum value:", max(d3.values()))

# 16. Find minimum value
print("16. Minimum value:", min(d3.values()))

# 17. Remove duplicate values
d4 = {"a": 10, "b": 20, "c": 10}
new_dict = {}
for key, value in d4.items():
    if value not in new_dict.values():
        new_dict[key] = value
print("17.", new_dict)

# 18. Print dictionary in reverse order
print("18. Reverse Order:")
for key in reversed(list(d3.keys())):
    print(key, ":", d3[key])

# 19. Create dictionary using loop
d5 = {}
for i in range(1, 4):
    d5[i] = i * i
print("19.", d5)

# 20. Count frequency of characters
text = "hello"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("20.", freq)

# 21. Convert dictionary keys into list
print("21.", list(d3.keys()))

# 22. Convert dictionary values into list
print("22.", list(d3.values()))

# 23. Check whether dictionary is empty
empty_dict = {}
print("23.", "Empty" if not empty_dict else "Not Empty")

# 24. Copy dictionary
copy_dict = d3.copy()
print("24.", copy_dict)

# 25. Clear dictionary
copy_dict.clear()
print("25.", copy_dict)