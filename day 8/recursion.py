""" def hello():
    print("hello world!")
    hello()
    
hello() """

def number(n=2):
    print(n)
    if n == 10:
        return
    number(n+1)
    
number()