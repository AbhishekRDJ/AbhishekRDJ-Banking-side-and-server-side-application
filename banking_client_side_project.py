def check_balance():
    print()
    print("___________________________________________________________________________________________________________________________")
    fobj = open("all_account.txt", "r")
    account_number = input(" Enter the Account Number: ").strip()
    Pin_number = input(" Enter the PIN number: ").strip()
    for i in fobj:
        ls = i.strip().split(" | ")
        print()
        if ls[3] == account_number and ls[4] == Pin_number:
            print("------------------- TOTAL Balance -------------------")
            print()
            print(f"User Name: {ls[1]}")
            print(f"Total Balance: {ls[2]} Rs")
            print("______________________________")
            break
            
    fobj.close()
    print()
    print("___________________________________________________________________________________________________________________________")

    
def transfer_amt():
    import datetime 
    '''
    
    accept account number and pin number
    if both matches then accept account number of 
    receiver. Send amount. 
    Before transferring, check sufficient balance
    '''
    def send(l1):
        nonlocal got  # Declare got as nonlocal to modify the outer scope variable
        for i, line in enumerate(all_lines):
            ls3 = line.strip().split(" | ")
            """print("Receiver Account in File:", ls3[3])"""
            if ls3[3] == reciver_acc:
                l1[2] = str(int(l1[2]) - int(amount))
                obj1.write(str(datetime.date.today())+" | " + "-"+str(amount)+" | "+str(sender_acc)+" | "+str(reciver_acc)+" | "+"Debit")
                ls3[2] = str(int(ls3[2]) + int(amount))
                obj2.write(str(datetime.date.today())+" | " + "+"+str(amount)+" | "+str(sender_acc)+" | "+str(reciver_acc)+" | "+"Credit")
                print("Updated Sender Balance:", l1[2])
                print("Updated Receiver Balance:", ls3[2])
                all_lines[i] = " | ".join(ls3) + "\n"
                got = True
                break



    print()
    print("___________________________________________________________________________________________________________________________")
    fobj = open("all_account.txt", "r+")
    all_lines = fobj.readlines()
    got = False
    sender_acc = input(" Enter the sender Account Number :")
    obj1=open(f"{sender_acc}.txt","a")
    Pin_sender = input(" Enter the PIN :")
    reciver_acc = input(" Enter the Receiver Account Number :")
    obj2=open(f"{reciver_acc}.txt","a")
    amount = input(" Enter the amount :")
    fobj.seek(0)
    for j,line in enumerate(fobj):
        ls = line.strip().split(" | ")
        if ls[3] == sender_acc and ls[4] == Pin_sender:
            if int(ls[2]) >= int(amount):
                send(ls)
                all_lines[j] = " | ".join(ls) + "\n"
    """print("Got:", got)"""
    if got:
        fobj.seek(0)  # Move the file pointer to the beginning
        fobj.truncate()  # Truncate the file
        fobj.writelines(all_lines)  # Write new content to the file
        fobj.close()  # Close the file
    else:
        print("---- Payment Fail ----")

    fobj.close()
    print()
    print("___________________________________________________________________________________________________________________________")




def change_pin():
    '''
	accept account number and pin number
	if both matches then:
		accept new pin
		re-enter new pin
	if both matches, then update original pin
    '''
    print()
    print("_________________________________________________________________________________________________")
    acc_no=input(" Enter the Account Number :")
    pin=input(" Enter the PIN :")
    fobj=open("all_account.txt" , "r+")
    ALL_lines=fobj.readlines()
    
    got = False
    for i, line in enumerate(ALL_lines):
        ls3=line.strip().split(" | ")
        if ls3[3]==acc_no and ls3[4]==pin:
            new_pin=input(" Enter the New Pin :")
            re_enter_pin=input(" Re-Enter the New Pin :")

            if new_pin==re_enter_pin:
                ls3[4]=new_pin
            ALL_lines[i] = " | ".join(ls3) + "\n"
            got = True
            print("PIN Changed ....")
            break
    
    print()
    
    if got:
        fobj=open("all_account.txt","w")
        fobj.writelines(ALL_lines)
    else:
        print("---- Something Went Wrong ----")
    print("_________________________________________________________________________________________________")
    fobj.close()

def view_transaction_history():
    print()
    print("_________________________________________________________________________________________________")
    acc_no=input(" Enter the Account Number :")
    pin_no=input(" Enter the PIN :")
    fobj=open(F"{acc_no}.txt" , "r")
    print("___________________________________ : Transaction History : ________________________________________")

    
    print("- - - - - - - - - - - - - - -")
 
    all_line=fobj.readlines()
    for i,line in enumerate(all_line):
        ls=line.strip().split(" | ")
        print("____________________________________________________________________________________________") 
        print(f" Date : {ls[0]} \t | Transaction : {ls[1]} \t | Process : {ls[2]}")
       
    print("_________________________________________________________________________________________________")
    fobj.close()
    
    

def view_account_info():
    '''
	accept account number and pin number
	if both matches then display account information
	like account holder's name, accout balance, 
	address, mobile number, email, etc...
    '''
    print()
    print("_________________________________________________________________________________________________")
    fobj=open("all_account.txt" , "r")
    account_number=input(" Enter the Account Number :")
    pin_number=input(" Enter the PIN :")
    print("- - - - - - - - - - - - - - -")
    
    for bh in fobj:
        ls1=bh.strip().split(' | ')
        
        if ls1[3]==account_number and ls1[4]==pin_number:
            print("Name :-",(ls1[1]) ,"\nAccount Balance :- ",ls1[2]," Rs","\nAccount Number :-",ls1[3])
        
    print("_________________________________________________________________________________________________")
    fobj.close()

while True:
    print("1 - Check Balance")
    print("2 - Transfer Amount")
    print("3 - Change PIN")
    print("4 - View Transaction History")
    print("5- View Account Information")
    print("6 - EXIT")
    ch = int(input("Provide your choice : "))
    if ch==1: check_balance()
    elif ch==2: transfer_amt()
    elif ch==3: change_pin()
    elif ch==4: view_transaction_history()
    elif ch==5: view_account_info()
    elif ch==6: exit(0)
