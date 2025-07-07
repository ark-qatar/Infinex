print("Enter 1 to ask only Question and Answer")
print("Enter 2 to ask True and False Question")
print("Enter 3 to ask Choose the Correct Answer type questions")

while (True):
    inp1 = int(input("Enter the Option: "))
    if (inp1 == 1):
        inp2 = input("Enter the Question: ")
        inp3 = input("Enter the Answer: ")
        print("Now the Computer will ask the question. Be ready!")
        print(inp2)
        inp2a = input("Enter your Answer: ")
        if (inp2a.upper() == inp3.upper()):
            print("You Won!")
        else:
            print("Try Again!")

    elif (inp1 == 2):
        inp4 = input("Enter the True/False Question: ")
        inp5 = input("Enter the correct answer (True or False): ")
        print("Now the Computer will ask the question. Be ready!")
        print(inp4)
        inp4a = input("Enter your Answer (True/False): ")
        if inp4a.upper() == inp5.upper():
            print("You Won!")
        else:
            print("You Lose!")

    elif (inp1 == 3):
        inp6 = input("Enter the MCQ Question: ")
        inp7 = input("Enter Option 1: ")
        inp8 = input("Enter Option 2: ")
        inp9 = input("Enter Option 3: ")
        inp10 = input("Enter Option 4: ")
        inp11 = int(input("Enter the correct option number (1-4): "))
        print("Now the Computer will ask the question. Be ready!")
        print(inp6)
        print("Option 1:", inp7)
        print("Option 2:", inp8)
        print("Option 3:", inp9)
        print("Option 4:", inp10)
        inp6a = int(input("Enter the Option number you think is correct: "))
        if (inp6a == inp11):
            print("You Won!")
        else:
            print("You Lose!")

    else:
        print("Invalid Option")

    uiop = input("Enter 'Q' to quit or any other key to continue: ")
    if (uiop.upper()) == "Q":
        break