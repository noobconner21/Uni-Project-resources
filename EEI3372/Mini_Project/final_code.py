#main class

class BankAccount:
    def __init__(self, account_number, initial_deposit):
        self.account_number = account_number
        self.balance = initial_deposit

    def deposit(self, amount): #deposit balance
        if amount <= 0:
            print("The deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited Rs.{amount} into account number {self.account_number}. New balance: Rs.{self.balance}")

    def withdraw(self, amount): #withdraw balance
        if amount <= 0:
            print("The Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount} from account number {self.account_number}. New balance: Rs.{self.balance}")

    def check_balance(self): #balance check
        print(f"Account number {self.account_number} balance: Rs.{self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

#create account
    def create_account(self, account_number, initial_deposit):  #account create
        if account_number in self.accounts:
            print("Account already exists.")
        elif initial_deposit <= 0:
            print("The Initial deposit can't be negative.")
        else:
            self.accounts[account_number] = BankAccount(account_number, initial_deposit)
            print(f"Account {account_number} created with initial deposit Rs.{initial_deposit}.")

    def deposit(self, account_number, amount): #deposit
        if account_number not in self.accounts:
            print("This Account does not exist. Please provide the correct account number")
        elif amount <= 0:
            print("The Deposit amount must be positive.")
        else:
            self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):  #withdraw
        if account_number not in self.accounts:
            print("This Account does not exist. Please provide the correct account number")
        elif amount <= 0:
            print("The Withdrawal amount must be positive.")
        else:
            self.accounts[account_number].withdraw(amount)

    def check_balance(self, account_number):  # check balance
        if account_number not in self.accounts:
            print("This Account does not exist. Please provide the correct account number")
        else:
            self.accounts[account_number].check_balance()

    def transfer(self, from_account_number, to_account_number, amount):  #transfer
        if from_account_number not in self.accounts or to_account_number not in self.accounts:
            print("1st or 2nd accounts do not exist. Please provide the correct account number")
        elif amount <= 0:
            print("The Transfer amount must be positive.")
        elif amount > self.accounts[from_account_number].balance:
            print("Insufficient balance for transfer.")
        else:
            print(f"\nTransferred Rs.{amount} from account number {from_account_number} to account {to_account_number}.\n")
            self.accounts[from_account_number].withdraw(amount)
            self.accounts[to_account_number].deposit(amount)

#user interface
def print_menu():
    print("\n----------Main Menu----------")
    print("\n1. Create new account")
    print("2. Check account balance")
    print("3. Withdraw money")
    print("4. Deposit money")
    print("5. Transfer money")
    print("6. Exit")
    print("\n-----------------------------")


def main():
    bank = Bank()

#user choice

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(account_number, initial_deposit)
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == "5":
            from_account_number = input("Enter account number to transfer from: ")
            to_account_number = input("Enter account number to transfer to: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer(from_account_number, to_account_number, amount)
        elif choice == "6":
            print("Exit.. Thank you for banking with us!..")
            break
        else:
            print("Invalid! Please enter a number between 1 - 6.")

#call main function
main()
