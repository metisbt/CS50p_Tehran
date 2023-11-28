import validators

if validators.email(input("What's your email address? ").strip()):
    print("Valid")
else:
    print("Invalid")