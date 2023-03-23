class ATM:

    def __init__(self):
        self.pin = "" 
        self.balance = 0
        self.manu()
        self.secret_word_one, self.secret_word_two, self.secret_word_three = "", "", "" # I want to add 3 secret word for each pin.

    def manu(self):

        user_input = input("""
        Hello, How may I help you?
        
        1. Press 1 to create pin.
        2. Press 2 to change pin.
        3. Press 3 to check balance.
        4. Press 4 to deposit.
        5. Press 5 to withdraw.
        6. Press 6 to show pin.
        7. Press 7 to exit.

        """)

        if user_input == "1":
            self.pin = self.create_pin()

        elif user_input == "2":
            self.pin = self.change_pin()

        elif user_input == "3":
            self.pin = self.check_balance()

        elif user_input == "4":
            self.pin = self.deposit()

        elif user_input == "5":
            self.pin = self.withdraw()

        elif user_input == "6":
            self.pin = self.show_pin()


        else:
            exit()
    # =================================================================================================
    def create_pin(self):

        user_pin = input("Please set your pin : ")
        if len(user_pin) > 3 and len(user_pin) < 5 :
            self.pin = user_pin


            secret_word_one = input("Please Enter your first secret word : ")
            self.secret_word_one = secret_word_one

            secret_word_two = input("Please Enter your second secret word : ")
            self.secret_word_two = secret_word_two

            secret_word_three = input("Please Enter your third secret word :")
            self.secret_word_three = secret_word_three

            print("Pin is created successfully.")
            self.manu()

        else:
            print("Pin must be 4 digit. Try again!")
            self.manu()
    # =================================================================================================
    def show_pin(self):


            secret_word_one = input("Enter your first secret word to see your pin :")

            if self.secret_word_one == secret_word_one:
                user_pin = input("Please enter your pin to see : ")
                if user_pin == self.pin:
                    print(f"Your pin number is {self.pin}")
                    self.manu()
                else:
                    print("You enter a wrong secret word. Try again!")
                    self.manu()
            else:
                print("You entered your first secret word wrong. Try again!")

    # =================================================================================================
    def change_pin(self):

        secret_word_two = input("Enter your second secret word to change your pin : ")
        if secret_word_two == self.secret_word_two :
            old_pin = input("Enter your old pin : ")
            if old_pin == self.pin :
                new_pin = input("Enter your new pin : ")
                self.pin = new_pin
                print("pin set successfully")
                self.manu()
            else:
                print("You enter a wrong password. Try again!")
                self.manu()
        else:
            print("You entered your second secret word wrong. Try again!")
            self.manu()

    # =================================================================================================

    def check_balance(self):

        user_pin = input("Please enter your pin : ")
        if user_pin == self.pin:
            print(f"Your current balance : {self.balance}")
            self.manu()

        else:
            print("You enter a wrong password. Try again!")
            self.manu()

    # =================================================================================================

    def deposit(self):
        attempt = 0
        while attempt < 3: # Here user can try 3 times to enter pin. If user enter wrong pin 3 times then it will redirect to main menu.
            user_pin = input("Please enter your pin : ")
            if user_pin == self.pin:
                deposit_balance = int(input("Enter the amount to deposit :  "))
                if type(deposit_balance) == int:
                    self.balance += deposit_balance
                    print(f"You deposit {deposit_balance} taka successfully." )
                    self.manu()

                else:
                    print("Please enter a valid number : ")
            else:
                if attempt < 2:
                    print("You enter a wrong password. Try again!")
                else:
                    print("You have exceeded the maximum number of attempts. Redirecting to main menu.")

                attempt += 1

        self.manu()

    # =================================================================================================

    def withdraw(self):
        attempt = 0
        while attempt < 3: # Here user can try 3 times to enter pin. If user enter wrong pin 3 times then it will redirect to main menu.
            secret_word_three = input("Enter your third secret word to withdraw money : ") # I want to ensure that user is the owner of this account.
            if secret_word_three == self.secret_word_three:
                user_pin = input("Please enter your pin : ")
                if user_pin == self.pin:
                    withdraw_balance = int(input("Enter the amount to withdraw :  "))
                    if type(withdraw_balance) == int :
                        if withdraw_balance >= self.balance:
                            print("You don't have enough balance. Please deposit some money. ")
                            print(f"Your current balance : {self.balance}")
                            self.manu()
                        else:
                            self.balance -= withdraw_balance
                            print(f"You withdraw {withdraw_balance} taka successfully. " )
                            print(f"Your current balance : {self.balance}")
                            self.manu()

                    else:
                        print("Please enter a valid amount. Try again! ")
                else:
                    if attempt < 2:
                        print("You enter a wrong password. Try again!")
                    else:
                        print("You have exceeded the maximum number of attempts. Redirecting to main menu.")
            else:
                if attempt < 2:
                    print("You enter a wrong secret word. Try again!")
                else:
                    print("You have exceeded the maximum number of attempts. Redirecting to main menu.")
            attempt += 1
        self.manu()

# =========================================================================================================================================

ibrahim = ATM()
print(ibrahim.secret_word_two)
