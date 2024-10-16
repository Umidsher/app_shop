def login():
    user_data = {
        'Umidsher': 'Usbekistan1991'
    }
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user_data and user_data[username] == password:
        return True
    else:
        print("Invalid username or password.")
        return False