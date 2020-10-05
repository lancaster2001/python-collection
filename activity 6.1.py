age = ("")

while age == (""):
    age = (input("please enter your age"))

if (int(age) > 16) and (int(age) < 65):
    print("age is valid")
else:
    print("age is invalid")
