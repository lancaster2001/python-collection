current_code = "0"
carry_on = "yes"
carry_on2 = ""
carry_on3= 0
current_code = ""

#-------------------------------------------------------------------------------
#subroutines below
#-------------------------------------------------------------------------------

#closing screen
#-------------------------------------------------------------------------------
def close():
    import turtle 

    ninja = turtle.Turtle()

    ninja.speed(9999999999999999)

    for i in range(180):
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)
    
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        
        ninja.right(2)
    
    turtle.done()
#security
#-------------------------------------------------------------------------------
def security():
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

#Calculator
#-------------------------------------------------------------------------------
def multiply(multiply1, multiply2):
    multiply_answer = multiply1 * multiply2
    print(multiply_answer)

def add(add1, add2):
    add_answer = add1 + add2
    print(add_answer)

def sub(sub1, sub2):
    sub_answer = sub1 - sub2
    print(sub_answer)

def div(div1, div2):
    div_answer = div1 / div2
    print(div_answer)

def calculator():
    type_calculator = input("+ - * or /")
    cal_num1 = int(input("enter a number"))
    cal_num2 = int(input("enter a second number"))
    
    if type_calculator == "*":
        multiply(cal_num1, cal_num2)
        
    if type_calculator == "+":
        add(cal_num1, cal_num2)
            
    if type_calculator == "-":
        sub(cal_num1, cal_num2)
            
    if type_calculator == "/":
        div(cal_num1, cal_num2)

#-------------------------------------------------------------------------------
#subroutines above
#-------------------------------------------------------------------------------

#Opening code
#-------------------------------------------------------------------------------

security()

while carry_on == ("yes" or "y" or "Y" or "YES"):

    carry_on3 = 0
    
    current_code = str(input("what code would you like to use?"))
#-------------------------------------------------------------------------------
#looking for requested script below---------------------------------------------
    if current_code == ("calculator" or "cal"):
        calculator()

    if current_code == ("n" or "" or "non" or " " or "/" or "'"):
        carry_on3 = 1
#looking for requested script above---------------------------------------------
#-------------------------------------------------------------------------------
    else :
        print("sorry that is not a script")
        carry_on3 = -1

    if carry_on3 == 0:
        carry_on = input("do you want to carry on?")
        carry_on2 = input("are you sure?")
        if carry_on2 == ("no" or "NO" or "n" or "N"):
            carry_on = "yes"
        if carry_on2 != ("no" or "NO" or "n" or "N"):
            close()
        
    if carry_on3 == 1:
        close()
