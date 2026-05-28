# findall

import re
string="I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy."
x=re.findall(r"happy",string)
print(x)

#search
y=re.search(r"happy",string)
print(y.start(),y.end())

#split
z=re.split(r" ",string)
print(z)

#sub
w=re.sub("happy","sad",string)
print(w)

#subn
e=re.subn("happy","sad",string)
print(e)

#caret
str1="Hello,World!"
s=re.findall("^Hello",str1)
print(s)

#dollar
q=re.findall(r"World!$",str1)
print(q)

#dot.
q=re.findall("He.lo",str1)
print(q)

#question mark
str3="mn"
x=re.findall("m?n",str3)
print(x)

#plus
str4="Hellooo"
s=re.findall("Hello+",str4)
print(s)

#+?
str5="From : using the : character"
x=re.findall("^F.+?:",str5)
print(x)

#*?
str5="From : using the : character"
x=re.findall("^F.*?:",str5)
print(x)

#*
str6="Hello World!"
x=re.findall("Hel*o",str6)
print(x)

#Alternation
str6="Hello World!"
x=re.findall("Hello | World!",str6)
print(x)

#Square brackets
str5="Hello World!"
x=re.findall("[^aeiou]",str5)
print(x)

#{m}
strc="Missipi Missipi Missipi"
d=re.findall(r"Missipi{3}",strc)
print(d)

