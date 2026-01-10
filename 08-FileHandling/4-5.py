# Main program that uses the emails module

from emails import email_sender, email_recipient, email_subject, email_body

file_name = 'email.txt'

try:
    # Read the email file
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    # Fetch data using functions
    print("Sender email:", email_sender(content))
    print("Recipient email:", email_recipient(content))
    print("Subject:", email_subject(content))
    print("Email body:")
    print(email_body(content))

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
