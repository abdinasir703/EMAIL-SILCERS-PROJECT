#EMAIL SLICER

email = input("Enter your email:")

index = email.index("@")

username = email[:index]

domain = email[index:]

print(f" username is {username} and domain is {domain}")
