while True:
    try:
        number = int(input("enter a number:"))
        s_number = int(input("enter a number:"))
        
        print(number/s_number)
        
    except ValueError():
        print("you did not enter the integer")
    
    except ZeroDivisionError():
        print("number canot be divied by zero")
        
    except Exception as e:
        # raise Exception ("unexpected error occured") 
        print("unexpected error",e)
        