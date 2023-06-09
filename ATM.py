import sys
class ATMMachine:

    def __init__(self):

        self.pin = ''
        self.balance = 00
        self.first_secret_word = ''
        self.second_secret_word = ''
        self.third_secret_word = ''

        print("Welcome to ATM Machine. Please create your pin number first to use this machine. ", end='\n\n')
        self.create_pin()

#=======================================================================================================================

    def manu(self):

        user_input = input("""
        
        1. Press 1 to change your pin number : 
        
        2. Press 2 to show your pin number : 
        
        3. Press 3 to check your balance : 
        
        4. Press 4 to deposit your balance : 
        
        5. Press 5 to withdraw your balance : 
        
        6. Press 6 to exit from your account : 
        
        """)

        if user_input == "1":
            self.change_pin()

        elif user_input == "2":
            self.show_pin_number()

        elif user_input == "3":
            self.check_balance()

        elif user_input == "4":
            self.deposit()

        elif user_input == "5":
            self.withdraw()

        else:
            sys.exit()

#=======================================================================================================================

    def create_pin(self):

        attempt = 1
        while attempt < 4: # this whlile loop give 3 attempt to create pin number
            user_pin = input("Enter your number to create pin : \n")
            if len(user_pin) < 5 and len(user_pin) > 3:  # Here we check pin is 4 digit or not
                self.pin = user_pin
                print("Your pin was created successfully. Now you can create your secret words.", end='\n\n')

                secret_word_one = input("Please enter your first secret word : \n")
                self.first_secret_word = secret_word_one

                secret_word_two = input("Please enter your second secret word : \n")
                self.second_secret_word = secret_word_two

                secret_word_three = input("Please enter your third secret word : \n")
                self.third_secret_word = secret_word_three
                print("Welcome Sir, Your pin was created successfully.")
                self.manu()

            else: # We give 3 attempt to create pin number otherwise it will exit from the program
                if attempt < 3: # it will give 3 attempt to create pin number
                    print(f"You must give 4 digit to create your pin. You have only {3 - attempt} chance.")

                else: # it user give wrong input 3 times then it will exit from the program with this message
                    print("You have used your maximum attempt. You are redirected to the out of ATM Machine.")
                    sys.exit()
            attempt += 1

# =======================================================================================================================
    def change_pin(self):  # change pin number and secret words
        attempt_for_secret_word = 1
        while attempt_for_secret_word < 4: # this while loop is for first secret word
            user_secret_word = input("Enter your first secret word to change your pin : \n")
            if user_secret_word == self.first_secret_word: # check first secret word is correct or not

                attempt_for_pin = 1
                while attempt_for_pin < 4:
                    user_pin = input("Enter your old pin number : \n")
                    if user_pin == self.pin: # check old pin match or not
                        attempt_for_len = 1
                        while attempt_for_len < 4: # we give 3 attempt to change pin number ortherwise
                            new_pin = input("Enter your new pin number : \n")
                            if len(new_pin) < 5 and len(new_pin) > 3:  # Here we check new pin is 4 digit or not
                                self.pin = new_pin
                                print("You changed your pin number successfully." , end='\n\n')
                                #===============================================================================
                                # Here we will ask user to change secret words or not for security purpose
                                user_opinion = input("Do you want to change your secret words : Y/N\n")
                                if user_opinion.upper() == "Y": # if user want to change secret words then this if will work
                                    ask_opinion = input("Which secret do you want to change : (first/ second/ third \n")
                                    if ask_opinion.lower() == "first": # if user want to change first secret word then this if will work
                                        new_secret_word_one = input("Enter the new first secret word : \n")
                                        self.first_secret_word = new_secret_word_one
                                        print("You changed your first secret word seccessfully.", end='\n\n')
                                        self.manu()

                                    elif ask_opinion.lower() == "second": # if user want to change second secret word then this if will work
                                        new_secret_word_two = input("Enter the new second secret word : \n")
                                        self.second_secret_word = new_secret_word_two
                                        print("You changed your second secret word seccessfully.", end='\n\n')
                                        self.manu()

                                    elif ask_opinion.lower() == "third": # if user want to change third secret word then this if will work
                                        new_secret_word_three = input("Enter the new thrid secret word : \n")
                                        self.third_secret_word = new_secret_word_three
                                        print("You changed your third secret word seccessfully.", end='\n\n')
                                        self.manu()

                                    else: # if user give wrong input to change secret words then this else will work
                                        print("Wrong input! Tri again.", end='\n\n')
                                        self.manu()

                                else: # if user don't want to change secret words then this else will work
                                    print("Thanks for your opinion Sir.", end='\n\n')
                                    self.manu()
                                #=================================================================================

                            else: # if the new greater than or less than 4 digit then this else will work
                                if attempt_for_len < 3:
                                    print(f"You must give 4 digit to create your pin. You have only {3 - attempt_for_len} chance.", end='\n\n')
                                else:
                                    print("You have used your maximum attempt to give your new pin. You are redirected to main manu.", end='\n\n')
                                    self.manu()
                            attempt_for_len += 1

                    else: # if old pin is wrong then this else will work and ask for new pin again
                        if attempt_for_pin < 3:
                            print(f"You entered a wrong password.You have only {3 - attempt_for_pin} chance.", end='\n\n')
                        else:
                            print("You have used your maximum attempt to give your old pin. You are redirected to main manu.", end='\n\n')

                    attempt_for_pin += 1
                self.manu()

            else: # if first secret word is wrong then this else will work
                if attempt_for_secret_word < 3:
                    print(f"You entered your first secret word wrong. You have only {3 - attempt_for_secret_word} chance.", end='\n\n')

                else:
                    print("You have used your maximum attempt to give your first secret word. You are redirected to main manu.", end='\n\n')
                    self.manu()
            attempt_for_secret_word += 1
# ======================================================================================================================
    def show_pin_number(self): # show pin number
        attempt_for_secret_word = 1
        while attempt_for_secret_word < 4: # this while loop is for second secret word to give 3 attempt to show pin number

            user_secret_word = input("Please enter your second secret word to show your pin : \n")
            if user_secret_word == self.second_secret_word: # check second secret word is correct or not
                attempt_for_pin = 1
                while attempt_for_pin < 4: # this while loop is for pin number to give 3 attempt to show pin number
                    ask_for_pin = input("Enter your pin number to show your pin : \n")
                    if ask_for_pin == self.pin: # check pin number is correct or not
                        print(f"Here is your pin number : {self.pin}", end="\n\n")
                        self.manu() # after showing pin number we will redirect to main manu

                    else: # if pin number is wrong then this else will work
                        if attempt_for_pin < 3:
                            print(f"You entered a wrong pin. You have only {3 - attempt_for_pin} chance.", end="\n\n")
                        else:
                            print("You have used your maximum attempt to show pin. You are redirected to main manu.",end='\n\n')
                            self.manu()
                    attempt_for_pin += 1 # this will increase the attempt for pin number
            else: # if second secret word is wrong then this else will work
                if attempt_for_secret_word < 3:
                    print(f"You entered your second secret word wrong. You have only {3 - attempt_for_secret_word} chance.", end='\n\n')
                else:
                    print("You have used your maximum attempt to give your first secret word. You are redirected to main manu.", end='\n\n')
                    self.manu()
            attempt_for_secret_word += 1 # this will increase the attempt for second secret word
#=======================================================================================================================
    def check_balance(self): # check balance
        attempt_for_secret_word = 1
        while attempt_for_secret_word < 4: # this while loop is for third secret word to give 3 attempt to check balance
            ask_for_secret_word = input("Please enter your third secret word to check balance : \n")
            if ask_for_secret_word == self.third_secret_word: # check third secret word is correct or not
                attempt_for_pin = 1
                while attempt_for_pin < 4: # this while loop is for pin number to give 3 attempt to check balance
                    ask_for_pin = input("Enter your pin number to check your balance : \n")
                    if ask_for_pin == self.pin: # check pin number is correct or not
                        print(f"Here is your balance : {self.balance}")
                        self.manu()
                    else: # if pin number is wrong then this else will work
                        if attempt_for_pin < 3:
                            print(f"You entered a wrong pin. You have only {3 - attempt_for_pin} chance.", end="\n\n")
                        else:
                            print("You have used your maximum attempt to check balance. You are redirected to main manu.",end='\n\n')
                            self.manu()
                    attempt_for_pin += 1 # this will increase the attempt for pin number
            else: # if third secret word is wrong then this else will work
                if attempt_for_secret_word < 3:
                    print(f"You entered your third secret word wrong. You have only {3 - attempt_for_secret_word} chance.", end='\n\n')
                else:
                    print("You have used your maximum attempt to give your third secret word. You are redirected to main manu.", end='\n\n')
                    self.manu()
            attempt_for_secret_word += 1 # this will increase the attempt for third secret word
        self.manu()

#=======================================================================================================================

    def deposit(self): # deposit money
        attempt_for_secret_word = 1
        while attempt_for_secret_word < 4: # this while loop is for first secret word to give 3 attempt to deposit money
            ask_for_secret_word = input("Please enter your first secret word to deposit balance : \n")
            if ask_for_secret_word == self.first_secret_word:
                attempt_for_pin = 1
                while attempt_for_pin < 4: # this while loop is for pin number to give 3 attempt to deposit money
                    ask_for_pin = input("Enter your pin number to deposit your balance : \n")
                    if ask_for_pin == self.pin:
                        attempt_for_amount = 1
                        while attempt_for_amount < 4: # this while loop is for amount to give 3 attempt to deposit money
                            ask_for_amount = input("Enter your amount to deposit : \n")
                            if ask_for_amount.isdigit():
                                self.balance += int(ask_for_amount)
                                print(f"You deposit {ask_for_amount} taka successfully.")
                                print(f"Your current balance is {self.balance} taka. ", end='\n\n')
                                self.manu()
                            else: # if amount is not digit then this else will work
                                if attempt_for_amount < 3:
                                    print(f"You must enter numbers only. You have only {3 - attempt_for_amount} chance.", end='\n\n')
                                else:
                                    print("You have used your maximum attempt to deposit your balance. You are redirected to main manu.",end='\n\n')
                                    self.manu()

                            attempt_for_amount += 1
                    else: # if pin number is wrong then this else will work
                        if attempt_for_pin < 3:
                            print(f"You entered a wrong pin. You have only {3 - attempt_for_pin} chance.", end="\n\n")
                        else:
                            print("You have used your maximum attempt to deposit your balance. You are redirected to main manu.",end='\n\n')
                            self.manu()
                    attempt_for_pin += 1
            else: # if first secret word is wrong then this else will work
                if attempt_for_secret_word < 3:
                    print(f"You entered your first secret word wrong. You have only {3 - attempt_for_secret_word} chance.",end='\n\n')
                else:
                    print("You have used your maximum attempt to give your first secret word. You are redirected to main manu.", end='\n\n')
                    self.manu()
            attempt_for_secret_word += 1
        self.manu()
#=======================================================================================================================

    def withdraw(self): # deposit money
        attempt_for_secret_word = 1
        while attempt_for_secret_word < 4: # this while loop is for first secret word to give 3 attempt to deposit money
            ask_for_secret_word = input("Please enter your first secret word to withdraw balance : \n")
            ask_for_secret_word_2 = input("Please enter your third secret word to withdraw balance : \n")
            if ask_for_secret_word == self.first_secret_word and ask_for_secret_word_2 == self.third_secret_word:
                attempt_for_pin = 1
                while attempt_for_pin < 4: # this while loop is for pin number to give 3 attempt to deposit money
                    ask_for_pin = input("Enter your pin number to withdraw your balance : \n")
                    if ask_for_pin == self.pin:
                        attempt_for_amount = 1
                        while attempt_for_amount < 4: # this while loop is for amount to give 3 attempt to deposit money
                            ask_for_amount = input("Enter your amount to deposit : \n")
                            if ask_for_amount.isdigit():
                                attempt_for_deposit = 1
                                while attempt_for_deposit < 4:
                                    if self.balance <= int(ask_for_amount):
                                        ask_for_deposit = input("You don't have enough balance to withdraw. Do you want to deposit your balance? (y/n) : \n")
                                        if ask_for_deposit == 'y':
                                            self.deposit()
                                        elif ask_for_deposit == 'n':
                                            print("You are redirected to main manu.", end='\n\n')
                                            self.manu()
                                        else:
                                            if attempt_for_deposit < 3:
                                                print(f"You must enter 'y' or 'n' only. You have only {3 - attempt_for_deposit} chance.", end='\n\n')
                                            else:
                                                print("You have used your maximum attempt to deposit your balance. You are redirected to main manu.",end='\n\n')
                                                self.manu()
                                    attempt_for_deposit += 1

                                self.balance -= int(ask_for_amount)
                                print(f"You withdraw {ask_for_amount} taka successfully.")
                                print(f"Your current balance is {self.balance} taka. ", end='\n\n')
                                self.manu()
                            else: # if amount is not digit then this else will work
                                if attempt_for_amount < 3:
                                    print(f"You must enter numbers only. You have only {3 - attempt_for_amount} chance.", end='\n\n')
                                else:
                                    print("You have used your maximum attempt to deposit your balance. You are redirected to main manu.",end='\n\n')
                                    self.manu()

                            attempt_for_amount += 1
                    else: # if pin number is wrong then this else will work
                        if attempt_for_pin < 3:
                            print(f"You entered a wrong pin. You have only {3 - attempt_for_pin} chance.", end="\n\n")
                        else:
                            print("You have used your maximum attempt to deposit your balance. You are redirected to main manu.",end='\n\n')
                            self.manu()
                    attempt_for_pin += 1
            else: # if first secret word is wrong then this else will work
                if attempt_for_secret_word < 3:
                    print(f"You entered your first secret word wrong. You have only {3 - attempt_for_secret_word} chance.",end='\n\n')
                else:
                    print("You have used your maximum attempt to give your first secret word. You are redirected to main manu.", end='\n\n')
                    self.manu()
            attempt_for_secret_word += 1
        self.manu()
#=======================================================================================================================

Ibrahim = ATMMachine()