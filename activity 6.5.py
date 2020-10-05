scores = [10, 20, 30, 40, 50]

scores_file = open("scores.txt","w")

for index in scores:
    scores_file.write("%s\n"%index)
    
scores_file.close()

scores_read = open("scores.txt", "r")

scores_read_array = scores_read.read()

print (scores_read_array)

scores_read.close()
