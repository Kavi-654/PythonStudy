a = [1,2,3,4,5,6,7,8,9,3,4,5]

print("Creating a Frozen Set:")
fset = frozenset(a)
print(fset)


# Membership check
print("\nMembership check:")
print(5 in fset)
print(100 in fset)

# Iterating through frozen set
print("\nIterating through Frozen Set:")
for item in fset:
    print(item)

# Set operations (allowed)
print("\nSet Operations:")
fset2 = frozenset([5,6,7,20,30])

print("Union:", fset.union(fset2))
print("Intersection:", fset.intersection(fset2))
print("Difference:", fset.difference(fset2))