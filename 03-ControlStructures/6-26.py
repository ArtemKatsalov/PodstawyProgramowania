correct_pin = "0000"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter the PIN code: ")
    if entered_pin == correct_pin:
        print("PIN correct. Access granted.")
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Incorrect...")
        else:
            print("Sorry, your payment card has been blocked.")
