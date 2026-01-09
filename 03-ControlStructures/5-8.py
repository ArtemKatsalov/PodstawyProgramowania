# atm.py - simple ATM simulation
PIN = '0000'
balance = 0 


while True:
        print("\nWelcome to the ATM!")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check PIN")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(f"Your current balance is: ${balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"${amount} deposited. New balance: ${balance}")
            else:
                print("Invalid amount. Please enter a positive number.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: $"))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"${amount} withdrawn. New balance: ${balance}")
                else:
                    print("Insufficient balance!")
            else:
                print("Invalid amount. Please enter a positive number.")
        elif choice == '4':
                    print(f"Youre actual PIN is {PIN}!")
        elif choice == '5':
            New_PIN = input('Enter new PIN: ')

            if New_PIN.isdigit():
                if New_PIN == PIN:
                    print(f"This is your actual PIN. Please enter a New 4-digit number : {New_PIN}")
                else:  
                    PIN = New_PIN
                    print(f"Youre PIN is changed. New PIN : {New_PIN}")   
            else:
                print("Invalid PIN. Please enter a 4-digit number.")
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5 or 6.")
