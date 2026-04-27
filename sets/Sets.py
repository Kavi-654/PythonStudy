a = [1,2,3,4,5,6,7,8,9,3,4,5]

# Creating a set (removes duplicates)
print("Creating a Set:")
set_b = set(a)
print(set_b)

# Adding elements
print("\nAdding elements:")
set_b.add(10)
print("After add:", set_b)

# Removing elements
print("\nRemoving elements:")
set_b.remove(3)   # removes specific element
print("After remove:", set_b)

# discard (safe remove)
set_b.discard(100)  # no error if element not present
print("After discard (no error):", set_b)

# pop (removes random element)
removed = set_b.pop()
print("Popped element:", removed)
print("After pop:", set_b)

# Set operations
print("\nSet Operations:")
set_c = {5,6,7,20,30}

print("Union:", set_b.union(set_c))
print("Intersection:", set_b.intersection(set_c))
print("Difference:", set_b.difference(set_c))

# Checking membership
print("\nMembership check:")
print(5 in set_b)
print(100 in set_b)

# Iterating through set
print("\nIterating through set:")
for item in set_b:
    print(item)

# Clearing set
set_b.clear()
print("\nAfter clear:", set_b)