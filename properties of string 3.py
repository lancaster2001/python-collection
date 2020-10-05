found = ""

my_string = input("input a word")

test_string = ""

input_word = input("what word do you want to look for in this word?")

for index in range (0 ,len(my_string) - 3):
 
    test_string = test_string + my_string[index]
    
    for test in range (1, len(input_word)):
        test_string = test_string + my_string[index + test]
        
    if test_string == (input_word):
        found = "yes"
        position = index
        
    test_string = ""
    
if found == "yes":
    print("it was found at index", position)
else:
    print ("sorry, word not found.")
