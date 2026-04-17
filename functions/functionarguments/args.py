# ==============================
# 1. Positional Arguments
# ==============================

def data(name, age):
    print("Positional -> Name:", name, "| Age:", age)


data("kavi", 23)


# ==============================
# 2. Default Arguments
# ==============================

def default_data(name, age=18):
    print("Default -> Name:", name, "| Age:", age)


default_data("kavi")        # uses default age
default_data("kavi", 25)    # overrides default


# ==============================
# 3. Keyword Arguments
# ==============================

def keyword_data(name, age):
    print("Keyword -> Name:", name, "| Age:", age)


keyword_data(age=30, name="John")


# ==============================
# 4. Mixed Arguments
# ==============================

def mixed_data(name, age):
    print("Mixed -> Name:", name, "| Age:", age)


mixed_data("kavi", age=28)   # positional + keyword


# ==============================
# 5. Variable Length Arguments (*args)
# ==============================

def var_args(*args):
    print("Var Args ->", args)


var_args(1, 2, 3, 4, 5)


# ==============================
# 6. Keyword Variable Length (**kwargs)
# ==============================

def var_kwargs(**kwargs):
    print("Var Kwargs ->")
    for key, value in kwargs.items():
        print(key, ":", value)


var_kwargs(name="kavi", age=23, role="developer")


# ==============================
# 7. Combination of All Types
# ==============================

def all_types(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


all_types(5, 20, 30, 40, name="kavi", role="developer")