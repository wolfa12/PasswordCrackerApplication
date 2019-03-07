# written in Python 3
# used https://www.w3schools.com/python/default.asp

# open text file of the most common passwords
file = open("passwords.txt", "r")

# create list
wordlist = []

# loop through the file and add them into a list
for line in file:
    wordlist.append(line)
