#timestable program with a function
def multiply(x,y):
    comment = "your answer is: "
    answer = x * y
    return comment, answer

#main program
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

answer = multiply(num1,num2)
print (answer)
