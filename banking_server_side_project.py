def view_acc_info():
    print()
    print("_________________________________________________________________________________________________")
    acc_no=input(" Enter the Account Number :")
    
    fobj=open(f"{acc_no}.txt" , "r")
    
    print("- - - - - - - - - - - - - - -")
 
    all_line=fobj.readlines()
    for i,line in enumerate(all_line):
        ls=line.strip().split(" | ")
        print("____________________________________________________________________________________________") 
        print(f" Date : {ls[0]} \t | Transaction : {ls[1]} \t | Process : {ls[2]}")
       
    print("_________________________________________________________________________________________________")
    fobj.close()

def withdrawal():
    import datetime
    print()
    print("_________________________________________________________________________________________________")
    acc_no=input(" Enter the Account Number :")
    fobj=open("all_account.txt","r+")
    fobj1=open(f"{acc_no}.txt","a")
    ALL_lines=fobj.readlines()
    
    got = False
    for i,line in enumerate(ALL_lines):
        ls=line.strip().split(" | ")
        if ls[3]==acc_no:
            amount=str(input(" Enter the Amount to Withdrawal :"))
            ls[2]=str(int(ls[2])-int(amount))
            fobj1.write("\n"+str(datetime.date.today())+" | "+"-"+str(amount)+" | "+str(acc_no)+" | "+str(acc_no)+" | "+"Withdrawls")
            ALL_lines[i] = " | ".join(ls) + "\n"
            got = True
            print("Amount Withdrawal ....")
            break
    print()
    
    if got:
        fobj=open("all_account.txt","w")
        fobj.writelines(ALL_lines)
    else:
        print("---- Something Went Wrong ----")
    print("_________________________________________________________________________________________________")
    fobj.close() 
    fobj1.close()   
    
    print()
    print("_________________________________________________________________________________________________")
    

    

def deposit():
    import datetime
    print()
    print("_________________________________________________________________________________________________")
    acc_no=input(" Enter the Account Number :")
    fobj=open("all_account.txt","r+")
    fobj1=open(f"{acc_no}.txt","a")
    ALL_lines=fobj.readlines()
    
    got = False
    for i,line in enumerate(ALL_lines):
        ls=line.strip().split(" | ")
        if ls[3]==acc_no:
            amount=str(input(" Enter the Amount to Deposit :"))
            ls[2]=str(int(ls[2])+int(amount))
            fobj1.write("\n"+str(datetime.date.today())+" | "+"+"+str(amount)+" | "+str(acc_no)+" | "+str(acc_no)+" | "+"Deposited")
            ALL_lines[i] = " | ".join(ls) + "\n"
            got = True
            print("Amount Deposited ....")
            break
    print()
    
    if got:
        fobj=open("all_account.txt","w")
        fobj.writelines(ALL_lines)
    else:
        print("---- Something Went Wrong ----")
    print("_________________________________________________________________________________________________")
    fobj.close() 
    fobj1.close()   
    
    print()
    print("_________________________________________________________________________________________________")
    

def fine_to_min_account():
    import datetime
    def per_account():
        fobj1=open(f"{acc}.txt","a")
        fobj1.write("\n"+str(datetime.date.today())+" | "+"-200"+" | "+str(acc)+" | "+str(acc)+" | "+ "Fine")
        fobj1.close()
        
    print()
    print("_________________________________________________________________________________________________")
    fobj=open("all_account.txt","r+")
    
    All_lines=fobj.readlines()
    got=False
    for i,line in enumerate(All_lines):
        ls=line.strip().split(" | ")
        if int(ls[2])<int(1000):
            ls[2]=str(int(ls[2])-int(200))
            acc=ls[3]
            per_account()
            All_lines[i] = " | ".join(ls) + "\n"
            got = True
            print("Fine Apply to Account ....")
            break
    print()
    
    if got:
        fobj=open("all_account.txt","w")
        fobj.writelines(All_lines)
    else:
        print("---- Something Went Wrong ----")
    print("_________________________________________________________________________________________________")
    fobj.close() 
      
    
    print()
    print("_________________________________________________________________________________________________")
    


def credit_interest():
    import datetime
    print()
    print("_________________________________________________________________________________________________")
    print("Enter to Apply Credit interest :")
    input()
    fobj=open("all_account.txt","r+")
    all_line=fobj.readlines()
    got=False
    
    for i,line in enumerate(all_line):
        ls=line.strip().split(" | ")
        interset=int(ls[2])*(5/100)
        credit=str(int(ls[2])+int(interset))
        ls[2]=credit
        acc=ls[3]
        
        # Check if the statement already exists in the file
        statement = f"{datetime.date.today()} | +{credit} | {acc} | {acc} | Credit Interest\n"
        if statement not in all_line:
            fobj1=open(f"{acc}.txt","a")
            fobj1.write("\n"+statement)
            print(f" Credit {credit} Deposit in {acc} Account.....")
        
    else:
        got=True
    print()
    if got:
        fobj=open("all_account.txt","w")
        fobj.writelines(all_line)
    else:
        print("---- Something Went Wrong ----")
    print("_________________________________________________________________________________________________")
    fobj.close() 
    fobj1.close()
    
    print()
    print("_________________________________________________________________________________________________")


def create_new_account():
    print()
    print("______________________________________________________________________________________________________________")
    fobj=open("all_account.txt","a")
    serial_number=input(" Enter the Serial Number :")
    Account_holder_name=input(" Enter the Account Holder Name  :")
    balance=str(0)
    account_number=input(" Enter the Account Number :")
    pin_number=input(" Enter the PIN :")
    fobj.write("\n"+str(serial_number)+" | "+str(Account_holder_name)+" | "+str(balance)+" | "+str(account_number)+" | "+str(pin_number))
    fobj1=open(f"{account_number}.txt","w")
    fobj1.close()
    fobj.close()
    print("---------------------------- Account is Created -------------------------------")
    print()
    print("________________________________________________________________________________________________________________")


while True:
    print("1 - Create New Account")
    print("2 - Credit Interest")
    print("3 - Fine to Minimum Balance")
    print("4 - Deposit")
    print("5 - Withdrawal")
    print("6 - View Account Information")
    print("7 - EXIT")
    ch = int(input("Provide your choice : "))
    if ch==1: create_new_account()
    elif ch==2: credit_interest()
    elif ch==3: fine_to_min_account()
    elif ch==4: deposit()
    elif ch==5: withdrawal()
    elif ch==6: view_acc_info()
    elif ch==7: exit(0)
