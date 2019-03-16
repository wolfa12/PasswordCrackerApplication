# written in Python 3
# used https://www.w3schools.com/python/default.asp

# open text file of the most common passwords
file = open("passwords.txt", "r")

# create list
wordlist = []

# loop through the file and add them into a list
for line in file:
    wordlist.append(line)



# ask user if they have any other words to add (don't add a duplicate word if it's there already)
def add_word(userword):

# ask user if they have words to delete
def delete_word(userword):
    print("hello world")

# ask user if they're asking for a specific word in the list (i.e. search for a word)
#prompt user 

def search_word(userword):
    if userword in wordlist:
        print("This word is in the existing list")
    else:
        print("This word doesn't exist in the list. Would you like to add it? Type yes or no")
        # add more to this later
print("hello world")