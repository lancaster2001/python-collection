password = ("")

while password == (""):
    password = input("please enter password")

if (len(password) > 8) and (len(password) < 13):
    print ("password is valid")
else:
    print ("password is invalid")
