PIN=1234
Balance=10000
for i in range(1,4):
    n=int(input("enter a PIN: "))
    if(PIN==n):
        print("your PIN is correct")
        break
    else:
        print(f"wrong PIN only {3-i} chances")
if(PIN!=n):
    print("Account Locked")
    exit()

while True:
    print("MENU")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    a=int(input("choose an option: "))
    if(a==1):
        print('1')
        print('Your Balance =',Balance)
    elif(a==2):
        print('2')
        b=int(input("enter the amount to deposit: "))
        if(b>0):
            Balance=Balance+b
            print("Your Balance =", Balance)
        else:
            continue
    elif(a==3):
        c=int(input("enter the amount to withdraw: "))
        if(c>Balance):
            print("Insufficient Balance")
        else:
            Balance=Balance-c
            print("Your Balance =", Balance)
    elif(a==4):
        print("Thank You !!")
        exit()
    else:
        print("Enter a valid Option")
    
    
    
        

    

        
