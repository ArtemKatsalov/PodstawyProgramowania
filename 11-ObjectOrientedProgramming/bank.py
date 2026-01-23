class BankAccount:
    def __init__(self, account_number):
        # store the account number
        self.account_number = account_number
        # initial balance is 0
        self.balance = 0.0

    def deposit(self, amount):
        # add amount to balance
        self.balance += amount
        print(f"Deposited: PLN {amount:.2f}")

    def withdraw(self, amount):
        # check if enough balance
        if amount > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance -= amount
            print(f"Withdrawn: PLN {amount:.2f}")

    def display_info(self):
        # format account number: first 2 digits, then groups of 4
        formatted_number = self.account_number[:2] + " "
        i = 2
        while i < len(self.account_number):
            formatted_number += self.account_number[i:i+4] + " "
            i += 4
        formatted_number = formatted_number.strip()

        print(f"Bank Account No: {formatted_number}")
        print(f"Balance: PLN {self.balance:.2f}")

def main():
    # create the bank account
    account = BankAccount("12345655559090111100007722")
    
    # display initial balance
    account.display_info()
    
    # deposit 25.30
    account.deposit(25.30)
    account.display_info()
    
    # attempt to withdraw 31.70
    account.withdraw(31.70)
    account.display_info()
    
    # withdraw 14
    account.withdraw(14)
    account.display_info()

if __name__ == "__main__":
    main()
