while (True):
    print("The thief is running")
    print("There are two officers choose one of them")
    user = int(input("Enter which officer should go to choose: "))
    if (user == 1):
        print("Oh! The thief got lost.")
        print("Try Again")
        break
    elif (user == 2):
        print("Nice! , now the thief took his car so what should the officer do")
        print("Enter 3 to go to Park")
        print("Enter 4 to stole someones car to find the thief")
        print("Enter 5 to go to a house")
        user2 = int(input("Enter the Number: "))
        if (user2 == 3):
            print("Oh! The thief is not their")
            print("Try Again")
            break
        elif(user2 == 4):
            print("Oh! You got killed by the car's owner")
            print("Try Again")
            break
        elif(user2 == 5):
            print("Oh Great! now you have reached at a house")
            print("Now someone is sitting")
            print("Enter 6 to sneak")
            print("Enter 7 to roll")
            user3 = int(input("Enter the Number: "))
            if(user3 == 6):
                print("Oh! The house owner got scared and kicked you outside of the house")
                print("Try Again")
                break
            elif(user3 == 7):
                print("Oh! now you got to a room and there you can see the thief stealing at the person's house")
                print("Enter 8 to shoot")
                print("Enter 9 to punch")
                user4 = int(input("Enter the Number"))
                if (user4 == 8):
                    print("Oh the theif attacked on you and took your gun and handcuffed you")
                    print("Try Again")
                    break
                elif(user4 == 9):
                    print("Wow! You caught the theif and Jailed Him")
                    break