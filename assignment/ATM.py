class ATM:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.favourite()
    def favourite(self):
        favourites=input("""please enter your choice
                    1 Enter 1 to pin genarate
                    2 Enter 2 to  deposit
                    3 Enter 3 to withdraw
                    4 Enter 4 to balance enquiry
                    5 Enter to exit: """)
        if favourites=="1":
            self.pin_genarate()
        elif favourites=="2":
            self.deposit()
        elif favourites=="3":
            self.withdraw()
        elif favourites=="4":
            self.balance_enquiry()
        elif favourites=="5":
            print("Welcome")
        else:
            print("invalid input")
    def pin_genarate(self):
        self.pin=input("Enter your pin : ")
        print("pin generate successfully")
        self.favourite()
    def deposit(self):
        temp=input("enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter your amount: "))
            self.balance=self.balance+amount
        else:
            print("invalid pin")
        self.favourite()
    def withdraw(self):
        temp=input("enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter your amount: "))
            self.balance=self.balance-amount
        else:
            print("invalid pin")
        self.favourite()
    def balance_enquiry(self):
        temp=input("enter your pin: ")
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        self.favourite()
atm=ATM()



