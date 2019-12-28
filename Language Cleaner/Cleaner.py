# Coded on 12/12/19 by Sourya Choudury

# Old dirty file
print("Enter the name of the file to clean.")
filename = input()

# Checking for bad words by referring to a file containing a large number of them
import json 
swear_words = json.load(open("words.json"))

text = open(filename)

string = ""

# New clean file
print("Enter the name of the new file you want to create.")
new_fname = input()
new_file = open(new_fname,"a+")

# Generating a clean file
for line in text:
    string = ""
    words = line.split()
    strg = "" 
    for word in words:
        strg = word.lower()
        if strg[0:len(strg)-1] in swear_words:
            string += word[0]+"*"*len(word[1:len(word)-2])+word[len(word)-2]+word[len(word)-1]+" "
        elif word.lower() in swear_words:
            string += word[0]+"*"*len(word[1:len(word)-1])+word[len(word)-1]+" "
        else:
            string += word+" "
    new_file.write(string+"\n")

new_file.close()

print("The cleaned text in contained in the file: ",new_fname)

# Closing the terminal after 5 seconds
import time
time.sleep(5)

