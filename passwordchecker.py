

class PasswordChecker:
    count = 0
#checks the password against length, uppercase, lowercase, digits, and symbols
    def check_password(self, user_password):
            isLength = self.check_password_length(user_password)
            isUppercase = self.check_uppercase(user_password)
            isLowercase = self.check_lowercase(user_password)
            isSymbol = self.check_symbol(user_password)
            isDigit = self.check_digits(user_password)
            isSequence = self.check_digit_sequence(user_password)
            print(isSequence)

            if(isLength):
                self.count +=1
            if not (isSequence):
                self.count +=1
            else:
                self.count -=1
            if(isUppercase):
                print("isssupercase")
                self.count +=1
            if(isLowercase):
                print("islovercase")
                self.count +=1
            if(isSymbol):
                print("issssymbol")
                self.count +=1
            if (isDigit):
                print("isssdigit")
                self.count += 1



            return self.count



    #checks to see if password is between 6 and 12 characters
    def check_password_length(self, password):
        isChecked = False
        if(len(password) < 6):
            print("Password length is less than the minimum of 6 characters")
        elif(len(password) > 12):
            print("Password length exceeds maximum length of 12 characters")
        else:
            isChecked = True

        return isChecked


    #checks to see if password contains uppercase
    def check_uppercase(self, password):
        isChecked = False
        for letter in password:
            if letter.isupper():
                isChecked = True
            else:
                print("Password does not contain any uppercase")
        print("uppercase:")
        print(isChecked)
        return isChecked

    #checks to see if password contains lowercase
    def check_lowercase(self, password):
        isChecked = False
        for letter in password:
            if letter.islower():
                isChecked = True
            else:
               print("Password does not contain any lowercase")
        print("lowercase:")
        print(isChecked)
        return isChecked


    #checks to see if password contains digit
    def check_digits(self, password):
        isChecked = False
        for letter in password:
            if letter.isnumeric():
                isChecked = True
            else:
                print("Password does not contain any digits")
        print("digits:")
        print(isChecked)
        return isChecked


    #checks to see if password contains symbol
    def check_symbol(self, password):
        isChecked = False
        symbol_list = ["!","@","#","&","%","*","?","/","~", "{", "}", "-", "_"]
        for letter in password:
            if letter in symbol_list:
                isChecked = True
            else:
                print("Password does not contain any symbols")
        print("symbol")
        print(isChecked)
        return isChecked

    def check_digit_sequence(self, s):
        pos = 0
        sequence = []
        while pos != len(s):
            try:
                value = int(s[pos])
            except ValueError:
                pos += 1
                sequence = []
                continue

            if not sequence:
                sequence.append(value)
            elif sequence[-1] + 1 == value:
                sequence.append(value)
                if len(sequence) == 3:
                    return sequence
            else:
                sequence = []
            pos += 1

        return []

