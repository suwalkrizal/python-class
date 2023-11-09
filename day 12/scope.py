# a = 10 

# def hello():
#     global a
#     a = 11
#     print(a)
    
   
# print(a)
# hello()
# print(a)


x=1

def outer():
    x=2
    def inner():
        global x
        x=3
        print("inner sees x as", x)
    inner()
    print("outer sees x as", x)
    
print("global sees x as", x)
outer()