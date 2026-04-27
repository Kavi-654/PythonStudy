from collections import namedtuple

Student =namedtuple('Student',['name','age','place'])

s=Student('James',45,'Kerela')
print(s)

#Accessing Operations
print("1. Access By Index")
print(s[1])

print("2. Access By Name")
print(s.name)

print("3.Access By getAttribute")
print(getattr(s,'age'))

#Conversion Operations

print("1.using _make()")

li=['Kavinaya','23','Chennai']
print(Student._make(li))

print("2.using asdict()")
li=["Hrithick",'1','Karaikudi']
print(s._asdict())

print("3.converting dictionary to named tuple")
di={'name':'Niki','age':'21','place':'chennai'}
print(Student(**di))

print("All fields of the Student are")
print(Student._fields)

print("Replacing the exisitng data")
print(s._replace(place='Chennai'))

print("3.creating a new instance for student")
print(Student.__new__(Student,'Hima','19','Bangalore'))
