""" def sum(a,b):
    return a+b """

""" sum= lambda a,b:a+b
    

print(sum(2,5)) """

""" def func(n):
    return lambda a:a*n

tripler=func(2)
print(doubler(3))
print(doubler(6))
print(doubler(9)) """

def func(n,b):
    return lambda a:a*n*b

tripler=func(3,4)
print(tripler(3))
print(tripler(6))
print(tripler(9))