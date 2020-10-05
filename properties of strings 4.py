carry_on = ("no")
if carry_on == ("no"):
    revision_notes = input("input your revision notes")
    carry_on = ("are you done?")

time_found = 0

found = ""

test_string = ""

input_word = ("variable")

for index in range (0 ,len(revision_notes) - 3):
 
    test_string = test_string + revision_notes[index]
    
    for test in range (1, len(input_word)):
        test_string = test_string + revision_notes[index + test]
        
    if test_string == (input_word):
        found = "yes"
        times_found = time_found + 1
        position = index
        
    test_string = ""

if found == "yes":
    print (input_word,"was found",times_found,"times")
