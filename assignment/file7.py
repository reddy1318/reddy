users={'vani':"reddy@123",'pavani':"vani@123"}
def login():
    username=input("Enter your username:")
    password=input("Enter your password:")
    if username in users and users[username]==password:
        print("login succeddful")
    else:
        print("invalid username or password.please try again")
login()