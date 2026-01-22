import queue

customer_queue = queue.Queue()

ticket_number = 1 

while True:
    print("\n1. New customer")
    print("2. Serve next customer")
    print("0. Quit")
    choice = input("Select an option: ")

    if choice == "1":
        # Add new customer with a ticket number
        print(f"Customer receives ticket number: {ticket_number}")
        customer_queue.put(ticket_number)
        ticket_number += 1

    elif choice == "2":
        # Serve the next customer
        if customer_queue.empty():
            print("No customers in the queue.")
        else:
            next_customer = customer_queue.get()
            print(f"Serving customer with ticket number: {next_customer}")

    elif choice == "0":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please choose 0, 1, or 2.")
