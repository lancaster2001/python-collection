first_name = ""
last_name = ""
full_name = input("inputyour full name example:first_name last_name")
for index in range (0 ,len(full_name) - 1):
    if full_name[index] == " ":
        position = index
for index in range (0 ,position): #-1
    first_name = first_name + full_name[index]
for index in range(position + 1 ,len(full_name) ): #-1
    last_name = last_name + full_name[index]
print (first_name)
print (last_name)
