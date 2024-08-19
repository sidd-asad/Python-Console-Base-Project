#BANK OPERATION USIN LOOP

class bank():
    bank_name="INDIAN BANK"
    Branch="Mumbra Thane "

    #create account   
    def __init__(self,username,pan,address):     #(constructor)
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f"Hello {username} cong! your account created successfully. ")

    #Deposit
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} deposit successfully. ")

    #Withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f"{amount} withdraw successfully .")
        else:
            print("insufficient Balance Please try again leter")

    #Mini_statement
    def Mini_statement(self):
        print(f"Your account Balance is {self.balance} ")



print(f"Welcome to {bank.bank_name} , {bank.Branch}")
username=input("Enter your name :")  #Account creation
pan=input("Enter your pan number : ")
address=input("Enter your address :")

b=bank(username,pan,address)    #Object creation

while True:
    print("Please Select any option :")
    print("1.deposit\n2.Withdraw\n3.MiniStatement\n4.Close ")
    option=int(input(""))

    if option==1:
        amount=eval(input("Enter deposited amount : "))
        b.deposit(amount)

    if option==2:
        amount=eval(input("Enter Withdraw amount :"))
        b.withdraw(amount)

    if option==3:
        b.Mini_statement()

    if option==4:
        print("Thanks for using Indian bank.. ")
        break
        
