# creating a tuple in python

a=(1,2,3,45)
print("One way of creating a tuple")
print(a)
b=tuple((7,8,9,10))
print("Another way of creating a tuple",b)

# concatenating a tuple
tup1=(3,4,5)
tup2=(6,7,8)
tup3=tup1+tup2
print(tup3)

# tuple unpacking with Asterick

tup=(1,2,3,4,5)
a,*b,c=tup
print(a)
print(b)
print(c)

# reversing a tuple has two methods

tup=(1,2,3,4,5)
print(tup[::-1])

print(tuple(reversed(tup)))