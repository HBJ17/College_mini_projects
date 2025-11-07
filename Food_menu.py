total_bill = 0

#Display choices

while True:  
    print("1.Pizza=150")
    print("2.Burger=100")
    print("3.Pasta=200")
    print("4.Fries=50")
    print("5.exit")
    
    #ask user to choose

    choice=int(input("Enter your choice:"))
    if choice == 1:
        n = int(input("Enter the number of items = "))
        total_bill += 150*n
        print("total bill is:",(total_bill))
    elif choice == 2:
        n = int(input("Enter the number of items = "))
        total_bill += 100*n
        print("total bill is:",(total_bill))
    elif choice == 3:
        n = int(input("Enter the number of items = "))
        total_bill += 200*n
        print("total bill is:",(total_bill))
    elif choice == 4:
        n = int(input("Enter the number of items = "))
        total_bill += 50*n
        print("total bill is:",(total_bill))
    elif choice == 5:
        if total_bill < 1000:
            print("total bill is:",(total_bill))
            print("Thank You, Visit Again")
            exit()
        else:
            if total_bill > 2000:
                total_bill = total_bill-(total_bill*0.5)
                print("Your discounted bill is:",(total_bill))
                print("Thank You, Visit Again")
                exit()
            elif total_bill < 2000:
                total_bill = total_bill-(total_bill*0.05)
                print("Thank You, Visit Again")
                exit()
    else:
        print("Enter the valid choice")






