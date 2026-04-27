from array import array

print("Creating an Array using array module:")

# 'i' → integer type
arr = array('i', [1, 2, 3, 4, 5])
print(arr)

# Adding elements
arr.append(6)
print("After append:", arr)

# Inserting element
arr.insert(2, 100)
print("After insert:", arr)

# Removing element
arr.remove(100)
print("After remove:", arr)

# Accessing elements
print("Element at index 0:", arr[0])

# Iterating
print("\nIterating array:")
for item in arr:
    print(item)