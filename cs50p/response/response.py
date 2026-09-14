import validators

if validators.email(input('what is your email')):
    print(True)
else:
    print(False)
