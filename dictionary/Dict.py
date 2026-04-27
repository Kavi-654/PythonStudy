# Creating a Dictionary

print("One way of creating dictionary:")
a = {1: 'geeks', 2: 'for', 3: 'geeks'}
print(a)

print("\nAnother way of creating Dictionary:")
# Correct syntax for dict()
b = dict({1: 'geeks', 2: 'for', 3: 'geeks'})
print(b)

# Removing Items From Dictionary
print("\nRemoving Items From Dictionary:")

# Using del
del b[1]   # removes key 1
print("After del:", b)

# Using pop()
print("\nDeletion of element using pop:")
b.pop(3)   # removes key 3
print("After pop:", b)

# Using popitem()
print("\nRemoving elements using popitem():")
b.popitem()   # removes last inserted item
print("After popitem:", b)

# Clearing dictionary
print("\nClearing the dictionary:")
b.clear()
print("After clear:", b)

# Iterating the Elements in the Dictionary
print("\nIterating the Elements in the Dictionary:")

print("\nUsing keys() method:")
for key in a.keys():
    print(key)

print("\nUsing values() method:")
for value in a.values():
    print(value)

print("\nUsing items() method:")
for key, val in a.items():
    print(key, ":", val)