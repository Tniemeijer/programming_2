# Good
"""
Excersise 2 from week 1.4
"""

l = [1,2,3,4,5]

def fn_1(x):
    return x * 2 

def fn_2(x):
    return x ** 2

def fn_3(data, *args):
    return [[arg(i) for i in data] for arg in args]

print(fn_3(l,fn_1,fn_2))

