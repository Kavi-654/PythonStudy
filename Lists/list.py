# creation of lists

a=[1,2,3]
print("method 1 for the creation of lists",a);

b=list((4,5,6,7))
print("method 2 for the creation of lists",b);

# methods in the list

# adding the elements int the list
a.append(8)
print("adding the Element:",a)

#inserting the element in the list

a.insert(2,9)
print("List after inserting new element at the specified index",a)

# removing the lement from the list
a.remove(9)
print("after removing the element from the list",a)

#poping the element from the list
c=b.pop(2)
print("popped element in the list",c)

#clearing the element from the list
b.clear()
print("after clearing the list",b)

#List comprehension concept
d=[4,5,6,7,8]
res=[a**2 for a in d]
print(res)
