print("welcome to the ATM")
account={'12':'1111'}
a=input("enter account nuumber:")
if a in account.keys():
    b=input("enter your pin:")
    if account[a]== b :
        print("login successful")
        account_details={"balance":1200,"transactions":[]}

        while True:
            print("chooose option:")
            print("1.Check balance")
            print("2.Deposit")
            print("3.withdraw")
            print("4.view transactios")
            print("5.Exit")
            choice=int(input("Enter your choice:"))
            if choice==1:
                print(f"your account balance is{account_details}")
            elif choice==2:
                 deposite=int(input("enter deposite amount:"))
                 account_details["balance"]=account_details.get("balance")+deposite
                 transsactions=account_details["transactions"].append(deposite)
                #  account_details["balance"].append(deposite)
                 print(account_details)
                 
            elif choice==3:
                withdraw=int(input("enter withdraw amount:"))
                account_details["balance"]=account_details.get("balance")-withdraw
                transsactions=account_details["transactions"].append(withdraw)

                print(account_details)
            elif choice==4:
                print("your transactions:")
                if account_details["transactions"]:
                    for transsactions in account_details["transactions"]:
                # account_details["transactions"].append(account_details['balance'])
                        print("your transsactions are",transsactions)

            elif choice==5:
                 print("EXIT")
                 break
    else:
        print("wrong pin number")
else:
    print("account number is incorrect")