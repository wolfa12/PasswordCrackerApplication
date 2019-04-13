# written in Python 3
# used https://www.w3schools.com/python/default.asp

# add in the pre-defined dictionary
def add_predefine:
    # open text file of the most common passwords
    file = open("passwords.txt", "r")
    # create list
    wordlist = []
    # loop through the file and add them into a list
    for line in file:
        wordlist.append(line)

# ask user if they have any other words to add (don't add a duplicate word if it's there already)
def add_word(userword):
    # check if the word is already in the list, if not, add it
    if userword not in wordlist:
        wordlist.append(userword)

# ask user if they have words to delete
def delete_word(userword):
    if userword in wordlist:
        wordlist.remove(userword)
    else:
        print("That word doesn't exist in the dictionary and cannot be deleted.")

# ask user if they're asking for a specific word in the list (i.e. search for a word)
def search_word(userword):
    if userword in wordlist:
        print("This word is in the existing list.")
    else:
        prompt = raw_input("This word doesn't exist in the list. Would you like to add it? Type yes or no")
        # add more to this later
        if prompt == "yes":
            word = raw_input("What word would you like to add?")
            add_word(word)
        elif prompt == "no":
            # move on
            print("Please continue.")
        else:
            print("Please type yes or no.")
