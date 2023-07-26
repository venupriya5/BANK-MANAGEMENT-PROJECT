print(5*" ",20*"***",5*" ")
print()
CUSTOMER_NAME=['priya','venu','Lalitha','Nagendra','Hemapriya']
CUSTOMER_ACCOUNTNUM=['YB12345','YB34235','YB87766','YB09987','YB09087']
CUSTOMER_IFSCODE=['YBN0','YBN1','YBN2','YBN3','YBN4']
CUSTOMER_BALANCE={'YB12345':1000,'YB34235':1000,'YB87766':2000,'YB09987':1000,'YB09087':'3000'}
Balance=0 #TO USE THIS VARIABLES WE DECLREAD IN STARTING.
Deposit=0
Withdraw=0
i=0
import random
while True:

    print(5*'_', "  WELCOME TO YES BANK " ,5*'_')
    print()
    print("> 1 Press  to get New Account")
    print("> 2 press  to get Balance details")
    print("> 3 press  to  Withdraw money ")
    print("> 4 press  to Deposit money ")
 
    Choose_num=int(input("Choose Your Required Number:"))
    '''the data given below are used to create account and print total details in order'''
    if Choose_num==1:
        print("You Are Selected To Open New Account")
        NAME=input(" ENTER YOUR FULL NAME:")
        Balance=int(input("ENTER DEPOSIT BALANCE:"))
        if NAME not in CUSTOMER_NAME:
            if Balance>=500:
                print("NAME:",NAME)
                r=(random.randint(123,453))# TO GET ACCOUNTNUM,IFSC CODE
                I=(random.randint(4,11))
                print(" ")
                print("-"*5,"Yes Bank Account ","-"*5)
                print("FULLNAME:",NAME)
                print('DEPOSIT BALANCE:',Balance)
                ACNUM=print("ACCOUNT_NUM:YB",end='')
                print(r)
                IFS=print("(IFSCCODE):YBN",end='')
                print(I)
                CUSTOMER_NAME.append(NAME)
                CUSTOMER_BALANCE.update[ACNUM]=(Balance)
                CUSTOMER_ACCOUNTNUM.append(ACNUM) 

                # WANT TO CHECK NEW ACCOUNT ADDED IN ABOVE LIST WE USE THIS METHODS, 
                # BY REQUIREMENTS WE REMOVE COMMENT AND RUN.
                #print(len(CUSTOMER_NAME)) 
                #print(len((CUSTOMER_BALANCE)))
                #print(CUSTOMER_BALANCE)     
                #print(len(CUSTOMER_ACCOUNTNUM))
                #print(len(CUSTOMER_IFSCODE))
            else:
                print(" ")
                print("NOT ALLOWED TO CREATE ACCOUNT,DEPOSIT ABOVE 499")
        break

    elif Choose_num==2:
        ''' BELOW DETAILS TO GET BALANCE DETAILS'''
        print(" You Selected To Check Balance Details")
        
        NAME=input("Enter full Name:")
        NUM=(input("Enter Account Number:"))
        IFSC=input("Enter IFSC CODE:")
        if NAME in CUSTOMER_NAME:
            if NUM in CUSTOMER_ACCOUNTNUM:
                 print("CUSTOMERBALANCE=",CUSTOMER_BALANCE[NUM], end=' ')
                    
        else:
            print("Invalid")
        break

    elif Choose_num==3:
        ''' IF WE FULL GIVEN DETAILS CORRECTLY WE GET PERMISSION TO WITHDRAW MONEY,
           OTHERWISE IT WILL PRINT ELSE BLOCK'''
    
        print("Your Choosing To Withdraw Money")
        NAME=input("Enter Full Name:")
        NUM=input("Enter Account Number:")
        IFSC=input("Enter IFSC CODE:")
        Withdraw=int(input("Enter Withdraw Amount:"))
        Balance=(CUSTOMER_BALANCE[NUM])
        print(Balance)

        if Balance>Withdraw:
            print("WITHDRAW_AMOUNT=",Withdraw)
            Balance=CUSTOMER_BALANCE[NUM]-Withdraw
            
            print("BALANCE=",Balance)
        else:
            print("Insufficient Balance, Please Deposit.")
        break

    elif Choose_num==4:

        print("Your Choosing Number Is To Deposit Money. Please Insert All Your Details")
        NAME=input("Enter full Name:")
        NUM=input("Enter Account Number:")
        IFSC=input("Enter IFSC CODE:")
        Deposit=int(input("Enter Deposit Amount:"))
        Balance=CUSTOMER_BALANCE[NUM]+Deposit
        print("Total Account Balance",Balance)
print(" ")
print("**"*5, "THANK YOU FOR CHOOSING YES BANK", "**"*5) #ENDED GREATINGS FOR CUSTOMERS
print("  "*5,20*"____","  "*5)       


    
                  
                  
                  
                  
            





