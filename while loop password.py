stored_password_open = open("password.txt", "r")
stored_password = stored_password_open.read()
stored_password_open.close()

password = ""

while (password == ""):
    
    password = input("please enter a password")
    if (password != stored_password):
        password = ""
        print("incorrect password")
    
    else:
     print("you've logged in")
    


#stored_password = open("password.txt","w")

#stored_password.write("%s"%"silentscopz1")

#stored_password.close()
