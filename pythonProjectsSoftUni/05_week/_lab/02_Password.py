user = input()
user_password = input()

while True:
    user_password_verification = input()
    if user_password_verification == user_password:
        print(f"Welcome {user}!")
        break
