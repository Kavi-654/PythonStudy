# ==============================
# 1. Local Variables
# ==============================

def get():
    a = 5   # local variable (exists only inside this function)
    print("Inside get() - local variable a:", a)

get()

# print(a)  ❌ This will cause error (a is not accessible outside)


# ==============================
# 2. Global Variable
# ==============================

b = 10   # global variable

def val():
    b = 30   # local variable (different from global b)
    print("Inside val() - local b:", b)

val()

print("Outside function - global b:", b)


# ==============================
# 3. Modifying Global Variable 
# ==============================

c = 100   # global variable

def modify():
    global c   # tells Python to use global c
    c = 200
    print("Inside modify() - modified global c:", c)

modify()

print("Outside function - updated global c:", c)
