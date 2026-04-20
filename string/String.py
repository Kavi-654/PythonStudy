s = "Geeks for Geeks"
p = "     Geeks"

# 1. Reverse the string using slicing [start:stop:step]
# A step of -1 traverses the string backward.
print(s[::-1])

# 2. Calculate the total number of characters (including spaces)
print(len(s))

# 3. Change the casing of the entire string
print(s.upper(), "|", s.lower())

# 4. Remove leading and trailing whitespace
print(p.strip())

# 5. Replace all occurrences of a substring with a new value
print(s.replace("Geeks", "Geek"))

# 6. Convert the string into a list of individual characters
char_list = list(s)
print(char_list)