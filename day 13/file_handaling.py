try:
    f = open('hello.txt','a')
    # print(f.read())
    f.write("\nlearning pYthon")
    f.close()
    
except FileNotFoundError:
    print('file not found')
    
except:
    print("An error occurred")