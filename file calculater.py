while True:


    try:
        Num1=((input("Enter your file:- ")))
        with open(Num1,"r") as Fopen:
            print(Fopen.read())
    except FileNotFoundError:
        print("Sorry but that file is not found.")
        User_choice=input("Would you like to Try again? Y or N:")
        if User_choice=="Y":
            continue
        else:
            break
