###This is a program that simulates an ATM machine. It allows the user to create a 4 digit pin, deposit or withdraw money, check their balance, change their pin, and exit the program. Additionally, there are three secret words associated with each pin that the user must know to perform certain actions.###

The program uses a class called ATM with a constructor that initializes the pin, balance, and calls the manu method which is used to display the options to the user and receive input. The manu method uses an if-else statement to determine what action the user wants to perform and calls the corresponding method.

The create_pin method is used to create a new pin for the user. The user inputs a 4 digit number, and three secret words that will be associated with the pin. If the input is valid, the pin and secret_word_one, secret_word_two, secret_word_three instance variables are updated, and the manu method is called.

The show_pin method asks the user to input the first secret word and pin number to show the pin. If the user inputs the correct secret word and pin, the pin is displayed, and the manu method is called. Otherwise, an error message is displayed, and the manu method is called again.

The change_pin method asks the user for their second secret word and old pin number to change the pin. If the user inputs the correct secret word and pin, they are prompted to enter a new pin number. The pin instance variable is updated, and the manu method is called. Otherwise, an error message is displayed, and the manu method is called again.

The check_balance method asks the user for their pin number to display their balance. If the user inputs the correct pin, their balance is displayed, and the manu method is called. Otherwise, an error message is displayed, and the manu method is called again.

The deposit method asks the user for their pin number and the amount they wish to deposit. If the user inputs the correct pin and a valid amount, their balance is updated, and the manu method is called. Otherwise, an error message is displayed, and the manu method is called again.

The withdraw method asks the user for their third secret word, pin number, and the amount they wish to withdraw. If the user inputs the correct secret word, pin, and a valid amount, their balance is updated, and the manu method is called. If the user attempts to withdraw more money than they have in their account, an error message is displayed, and the manu method is called again. If the user enters the incorrect secret word or pin number, they have up to 3 attempts to enter the correct information before being redirected to the main menu.
