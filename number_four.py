#WITI Academy is proposing a sacco to help students save their money.
#Design a platform that will do the following.
#Welcome to,WITI Academy Sacco.
#1.Deposit Money
#2.Withdraw Money
#3.Check Balance
#Ensure if the student selects 1,money is deposited and the minimum deposit should be 1000.
#If the student selects 2,money should be withdrawn and a minimum withdrawal is 500.
#If the student selects 3,the account balance should de displayed.
# WITI Academy SACCO System 
         #solutions
def sacco_transactions():

    account_balance = 0 #Initial account_balance is 0
    run = 1
    while run == 1: #while loop
        print("\nWelcome to,WITI Academy Sacco")
        print("1.Deposit Money")
        print("2.Withdraw Money")
        print("3.Check Balance")
        
        student_choice = int(input("Please enter your choice(1,2,or 3):"))

        if student_choice == 1:
            print("\n....Processing a deposit transaction....")
            deposit_amount  = int(input("Enter amount to be deposited:"))
            if deposit_amount < 1000:
                print("\nMinimum deposit is 1000")
            else:
                account_balance += deposit_amount #same as account_balance = account_balance + deposit_amount
                print(f"Dear student, You have deposited {deposit_amount: ,} and Your new account balance is {account_balance: ,}")

        elif student_choice == 2:
            print("\n....Processing a withdraw transaction....")
            withdraw_amount = int(input("Enter amount to be withdrawn:"))
            if account_balance == 0:
                print("Your balance is 0")
            elif withdraw_amount <500:
                print("Minimum withdraw amount is 500")
            elif withdraw_amount > account_balance:
                print(f"Withdraw failed, insufficient funds.")
            else:
                account_balance -= withdraw_amount #same as account_balance = account_balance - withdraw_amount
                print(f"Dear student,You have withdrawn {withdraw_amount: ,} and Your new account balance is {account_balance: ,}")

        elif student_choice == 3:
            print(f"Your account balance is {account_balance: ,}")
        else:
            print("You entered a wrong choice! Please select 1,2 or 3\n")

        run = int(input("Enter 1 to continue or any number to exit:"))

        if run != 1:
            print(f"Thanks for using our Sacco.")
            break

sacco_transactions()
