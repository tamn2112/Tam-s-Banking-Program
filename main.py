from authentication import registration
from profile_creating import UserProfile
from banking import Banking
from greetings import Greetings

def main():
    # Greeting user
    someGreetings = Greetings()
    print(someGreetings.WELCOME_BANNER)

    # Authentication 
    start_Authentication = registration()
    print(start_Authentication)
    
    # Creating Profile
    user_profile = UserProfile()
    user_profile.get_user_info()
    filename = 'profile_database.txt'
    user_profile.save_to_file(filename)
    print("Thank you for creating your profile!")

    # Start asking for options from Banking
    print(("Welcome to your account!"))
    newBankAccount = Banking(0)
    # Create a banking account
    print("Your current balance is 0. Please make your initial deposit.")
    while True:
        initial_deposit = float(input('Please enter your first amount of deposit (nonnegative): '))
        if newBankAccount.verify_deposit_amount(initial_deposit):
            print("Deposit successful!")
            # deposit 
            newBankAccount.deposit(initial_deposit)
            # display new total balance
            print(newBankAccount.display())
            break
        else:
            print('Invalid deposit amount. Please try again.')

    # Going into other options
    
    while True:
        option = int(input("Please enter 1 for withdraw, 2 for deposit, 3 for exit: "))
        if option == 1:
            while True:
                amount = int(input("Please enter withdrawing amount: "))
                if newBankAccount.verify_sufficient_fund(amount) == False:
                    print("Insuffcient fund. Please choose other option.")
                else:
                # withdraw
                    newBankAccount.withdraw(amount)
                    print('Withdrawal successful.')
                # display new total balance
                    print(newBankAccount.display())
                    break

        elif option == 2:
            while True:
                amount = int(input("Please enter amount to deposit (nonnegative): "))
                if newBankAccount.verify_deposit_amount(amount):
                    print("Deposit successful!")
                    # deposit
                    newBankAccount.deposit(amount)
                    # display new total balance
                    print(newBankAccount.display())
                    break
                else:
                    print("Invalid deposit amount. Please try again")
             
        elif option == 3:
            print(someGreetings.GOODBYE_MESSAGE)
            break

if __name__ == "__main__":
    main()



