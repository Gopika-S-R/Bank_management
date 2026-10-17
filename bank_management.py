class Bank:
    def __init__(self):
        self.accounts=[]

    def create_account(self):
        account_no=int(input("enter the account number:"))

        for acc in self.accounts:
            if acc["account_no"]==account_no:
                print("account already exist ")
                return
            
        name=(input("enter the name:"))
        balance=float(input("enter the initial balance:"))
        if balance<500:
            print("minimum intial balance should be 500")
        else:
            account={
                "account_no":account_no,
                "name":name,
                "balance":balance
                }
            self.accounts.append(account)
            print("Account created successfully")


    def display_accounts(self): 
        if self.accounts:       
            for account in self.accounts:
                print(f"Account no    :{account['account_no']}")
                print(f"Customer name :{account['name']}")
                print(f"Balance       :{account['balance']}")
                print("----------------------------")
        else:
             print("no accounts found")

    def search_account(self):
        account_no=int(input("enter the no to search:"))
        for account in self.accounts:
            if account['account_no']==account_no:
                print(f"Account no    :{account['account_no']}")
                print(f"Customer name :{account['name']}")
                print(f"Balance       :{account['balance']}")
                break
        else:
            print("Account not exist")

    def update_account(self):
        account_no=int(input("enter the account no:"))
        for account in self.accounts:
            if account['account_no']==account_no:
                print("1.Update Customer Name")
                print("2.Update Account Number")
                choice=int(input("enter your  choice:"))
                if choice==1:
                    new_name=input("enter the new customer name:")
                    account["name"]==new_name
                    print("Customer name updated")
                elif choice==2:
                    new_acc_no=int(input("enter the new account no:"))
                    for acc in self.accounts:
                        if acc['account_no']==new_acc_no:
                            print("Account already exist")
                            break 
                    else:
                        account['account_no']=new_account_no
                        print("Account number updated")
        else:
            print("Account not found")
            

    def deposit_amount(self):
        account_no=int(input("Enter the account number:"))
        for account in self.accounts:
            if account['account_no']==account_no:
                amount=float(input("enter the deposit amount:"))
                if amount>0:
                    account['balance']+=amount
                    print(f"Deposit amount: {amount}")
                    print(f"Current balance: {account['balance']}")
                else:
                    print("Deposit amount must be greater than 0")
                return
        else:
            print("Account not foound")

    def withdraw_amount(self):
        account_no=int(input("Enter the account no"))
        for account in self.accounts:
            if account['account_no']==account_no:
                amount=float(input("enter the withdrawal amount"))
                if amount>0:
                    if account['balance']-amount>500:
                        account['balance']-=amount
                        print(f"Withdrawal amount: {amount}")
                        print(f"Current balance: {account['balance']}")
                    else:
                        print("Accont must maintain a  minimum balance of 500")
                else:
                    print("Withdrawal amount muust be greater than zero")
                return
        else:
            print("accoutn not found")

    def delete_account(self):
        account_no=int(input("Enter the account no:"))
        for account in self.accounts:
            if account['account_no']==account_no:
                if account['balance']>0:
                    print("accont cannot be deleted")
                else:
                    self.accounts.remove(account)
                    print(f"account with account_no {account_no} is deleted")
                return
        else:
            print("Account not found")

        





            

b1=Bank()

print("====================Bank Management System ============")
while True:
    print("1.Create Account")
    print("2.isplay Accounts")
    print("3.Search Account")
    print("4.Update Account")
    print("5.Deposit")
    print("6.Withdraw")
    print("7.Delete Account")
    print("8.Exit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        b1.create_account()
        print("-------------------------")
    elif choice==2:
        b1.display_accounts()
        print("-------------------------")
    elif choice==3:
        b1.search_account()
        print("-------------------------")
    elif choice==4:
        b1.update_account()
        print("-------------------------")
    elif choice==5:
        b1.deposit_amount()
        print("-------------------------")
    elif choice==6:
        b1.withdraw_amount()
        print("-------------------------")
    elif choice==7:
        b1.delete_account()
        print("-------------------------")
    elif choice==8:
        print("thank you")
        break
    else:
        print("invalid choice")


# --------------------------------------------------

