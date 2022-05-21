#Simple bank app
import random
#Initializing app
database = {}
def init():

    response = False
    print("Welcome to Bank Ruby!")

    while response == False:
        validResponse = int(input("Do you have an account with us? Reply 1 for Yes and 2 for No : \n"))
        if (validResponse == 1):
            response = True
            login()
        elif (validResponse == 2):
            response = True
            register()
        else:
            print("Please Input a Valid response")


#Registration
def register():
    print("****Register here******")
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    email = input("Enter Email address: ")
    password = input("Create password: ")
    account_number = accountNumberGenerator()
    account_balance = 0.00


    database[account_number] = [first_name, last_name, email, password, account_balance]
    print("Registration Successful!! Your account number is %i " %account_number)

    login()




#Login
def login():

    
    print("Login here")
    user_id = int(input("Enter Account Number: "))
    user_password = input("Enter Password: ")
        
    for account_number,userDetails in database.items():
        if(account_number == user_id):
            if(userDetails[3] == user_password):
                account_validity = True
                transaction(userDetails)
            
    print("Invalid Account Number or Password")
    login()


#Perform Transaction
def transaction(user):
    print("Welcome %s %s. What would you like to do today? " %(user[0],), user[1])
    

    selection = int(input("Select 1 to Check Balance, 2 for Withdrawal, 3 for Deposit 4 to Logout and 5 to Exit: \n"))
    
    if (selection == 1 ):
        account_balance_function()
    elif(selection == 2):
        withdrawal()
    elif(selection == 3):
        deposit()
    elif(selection == 4):
        login()
    elif(selection == 5):
        exit()
    else:
        print("Invalid Selection")
        transaction(user)

#Account balance check
def account_balance_function(user):
    print("Your account balance is %i" %user[4])
    option = False

    while (option == False):
        any_other = int(input("Would you like to perform any other transaction? 1(Yes) or 2(No)"))
        if (any_other == 1):
            option = True
            transaction(user)
        elif(any_other ==2):
            option = True
            exit()
        else:
            print("Inavlid option selected")

#Withdrawal
def withdrawal(user):
    withdrawal_amount = int(input("How much would you like to withdraw? \n"))
    if (withdrawal_amount > user[4]):
        print("You cannot withdraw more than your current account balance!!!")
    else:
        account_balance = user[4] - withdrawal_amount
        print("Withdrawal Successful. Your account balance is %i" %account_balance)

    option1 = False

    while (option1 == False):
        any_other =int(input("Would you like to perform any other transaction? 1(Yes) or 2(No)"))
        if (any_other == 1):
            option1 = True
            transaction(user)
        elif(any_other ==2):
            option1 = True
            exit()
        else:
            print("select a valid option")
#Deposit
def deposit():
    deposit = int(input("How much would you like to deposit? \n"))
    account_balance = account_balance + deposit
    print("Deposit Successful. Your account balance is %i"%account_balance)

    option2 = False
    while (option2 == False):
        any_other =int(input("Would you like to perform any other transaction? 1(Yes) or 2(No)"))
        if (any_other == 1):
            option2 = True
            transaction(user)
        elif(any_other ==2):
            option2 = True
            exit()
        else:
            print("Select a valid option")



#Account number generator
def accountNumberGenerator():
    return random.randrange(1111111111,9999999999)

init()
