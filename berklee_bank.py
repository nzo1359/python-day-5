bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}



'''

Name: name
Task: check if the name being input matches a name in the system database
Input: ask for user's name
Side effects: input "Please enter your name here: "
Return: Return the username. If entered name matches a key from bank_dict, proceed to pin. If entered name is invalid, input name again.

'''




'''

Name: pin
Task: assign a PIN number to each key, or user name.
Input: ask for user's PIN number
Side effects: input "Please input your PIN number: "
Return: if entered PIN matches the correct user's pin, proceed to menu. If entered PIN is invalid, input pin again. 

'''




'''

Name: balance
Task: keep track of current user's balance value.
Input: -
Side effects: print current user's current balance.
Return: -

'''





'''

Name: deposit
Task: adds input value to current user's balance
Input: input "How much would you like to deposit?"
Side effects: print "'input value' has been deposited to your balance."
Return: add input value to current user's balance.

'''



'''

Name: withdraw
Task: substracts input value from current user's balance
Input: input "How much would you like to withdraw?"
Side effects: print "'input value' has been withdrawn from your balance."
Return: substract input value from current user's balance.

'''




'''

Name: quit
Task: end the program
Input: input "Would you like to quit the program?"
Side effects: if input value = 'Yes', print "Thank you for using Berklee ATM. Have a nice life."
Return: end the program

'''



def print_welcome():
    print("Welcome to Berklee ATM")


def get_username():
    name = input("What is your name?")
    return name


def get_pin():
    pin = input("Please input your pin: ")
    return pin


def verify_identity(username, pin):
    if bank_dict.get(username):
        users_values = bank_dict.get("pin")
        return True
    print("Access denied for ", username, "with pin", pin)



def get_menu_choice():
    choice = input("Would you like to deposit, withdraw or quit")
    return choice

def get_balance(username):
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        balance = users_values.get("balance")
        print()
    return None


def deposit_money(username):
    deposit_amount = int(input("Deposit amount: "))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_balance = users_values.get("balance")
        new_balance = previous_balance + deposit_amount
        users_values.update({"balance": new_balance})

    return None


def withdraw_money(username):
    withdraw_amount = int(input("Withdraw amount: "))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_balance = users_values.get("balance")
        new_balance = previous_balance - withdraw_amount
        if new_balance < 0:
            print("Insufficient funds")
        else:
            users_values.update({"balance": new_balance})

    return None






def run_unit_tests():
    #withdraw_money("Priya")         # ask for amount, if 200 fail
    #withdraw_money("Priya")         # ask for amount, if 100 succeed
    #deposit_money("Priya")          # ask for amount, if 100 succeed

    #get_balance("Priya")            # print $100

    #verify_identity("Priya", "4821")    # expecting successful login
    #verify_identity("Priya", "0000")    # expecting fail login

    #print_welcome()                 # expecting print welcome message
    #get_pin()                       # expecting it to ask for pin
    #get_username()                  # expecting it to ask for username







def main():
    print_welcome()
    name = get_username
    pin = get_pin
    valid = verify_identity(name, pin)
    if not valid:
        return

    while True:
        users_choice = get_menu_choice()
        if users_choice == "balance":
            get_balance(name)
        elif users_choice == "withdraw":
            withdraw_money(name)
        elif users_choice == "deposit":
            deposit_money()
        elif users_choice == "quit":
            break



main()



