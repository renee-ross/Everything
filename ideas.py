#This is my ideas for my everything

#for reading and modifying the ideas txt file

#to get the total number of lines in the file
counter = 1

#opening file to read
f = open("ideas.txt", "r")
# Reading from file, counting the line breaks
Content = f.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        counter += 1
#printing the list
print(Content)
f.close()

#opening file to append
f = open("ideas.txt", "a")
idea = input("Add item to the ideas list: ")
f.write('\n' + str(counter) + ". " + idea)
f.close()

#reopening file to read
f = open("ideas.txt", "r")
#printing the new list
print(f.read())
f.close()