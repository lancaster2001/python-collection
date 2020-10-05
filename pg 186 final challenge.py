hard_disk = ["c 1","","a 2","b 3","c 4","c 2","","a 3","","b 1","","b 2","c 3","c 5","a 1","",]
hard_disk_split = ["","","","","","","","","","","","","","","",""]
hard_disk_correct = ["","","","","","","","","","","","","","","",""]
file_letters = ["a","b","c"]
file_numbers = ["1","2","3","4","5"]
thing = -1

for index in range (0 , len(hard_disk)):
    hard_disk_split[index] = hard_disk[index].split(' ', 1)

for file_letter_arranger in range (0,3) :
    for file_number_arranger in range (0,5):
        for index in range (0 , len(hard_disk)):
            if hard_disk_split[index][0] == file_letters[file_letter_arranger] :
                if hard_disk_split[index][1] == file_numbers[file_number_arranger] :
                    thing = thing + 1
                    hard_disk_correct[thing] = hard_disk[index]

for index in range (0 , 11):
    hard_disk_correct[index] = hard_disk_correct[index].replace(" ","")

print (hard_disk_correct)
