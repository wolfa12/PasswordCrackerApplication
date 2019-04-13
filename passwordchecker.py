
#checks the password against length, uppercase, lowercase, digits, and symbols
def check_password():
    user_password = input("Please enter a password: ")
    isLength = check_password_length(user_password)
    if(isLength):
        isUppercase = check_uppercase(user_password)
    if(isUppercase):
        isLowercase = check_lowercase(user_password)
    if(isLowercase):
        isSymbol = check_symbol(user_password)
    if(isSymbol):
            print("Password is acceptable for use")

#checks to see if password is between 6 and 12 characters
def check_password_length(password):
    isChecked = False
    if(password.length < 6):
        print("Password length is less than the minimum of 6 characters")
    elif(password.length > 12):
        print("Password length exceeds maximum length of 12 characters")
    else:
        isChecked = True

    return isChecked


#checks to see if password contains uppercase
def check_uppercase(password):
    isChecked = False
    for letter in password:
        if letter.isupper():
            isChecked = True
        else:
            print("Password does not contain any uppercase")

    return isChecked

#checks to see if password contains lowercase
def check_lowercase(password):
    isChecked = False
    for letter in password:
        if letter.islower():
            isChecked = True
        else:
            print("Password does not contain any lowercase")
    return isChecked


#checks to see if password contains digit
def check_digits(password):
    isChecked = False
    for letter in password:
        if letter.isnumeric():
            isChecked = True
        else:
            print("Password does not contain any digits")
    return isChecked


#checks to see if password contains symbol
def check_symbol(password):
    isChecked = False
    symbol_list = ["!","@","#","&","%","*","?","/","~"]
    for letter in password:
        if letter in symbol_list:
            isChecked = True
        else:
            print("Password does not contain any symbols")
    return isChecked
