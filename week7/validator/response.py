from validator_collection import is_email

email_address = input("What's your email address? ")

if is_email(email_address):
    print("Valid email address")
else:
    print("Invalid email address")
