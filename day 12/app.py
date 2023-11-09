users=[

]

islogin=False

def register(username, password):
    user={
        'username':username,
        'password':password 
    }
    users.append(user)
    # print(user)


def login(username, password):
    for user in users:
        if username == user['username'] and password == user['password']:
            global islogin
            islogin = True
            return
        print("No credential match")

def checklogin():
    if islogin:
        print("user is logged in ")
    else:
        print("user have't logged in yet !!!")  
    


while True:
    print(users)
    choice = int(input(""" 
        Enter any choices
        1.press 1 to login
        2.press 2 to check if user is logged in or not
        """))

    if choice == 1:
        username = input("Enter Username:")
        password = input("Enter password:")
        login(username, password)
        
    if choice == 2:
        username = input("Enter Username:")
        password = input("Enter Password:")
        register(username, password)
    else:
        checklogin()
        


# login agadi tapai register
# register username unique
# show all the user (user must logged in)
 