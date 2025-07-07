# AR CALCULATOR
inp1 = float(input("Enter the float or decimal type number to calculate: "))
inp2 = input("Enter the operator you want to use + , - , * , /: ")
inp3 = float(input("Enter the  2nd float or decimal type number to calculate: "))
if (inp2 == "+"):
    ab = inp1 + inp3
    print("The Sum of: " , ab)
elif (inp2 == "-"):
    cd = inp1 - inp3
    print("The Subtraction of: " , cd)
elif (inp2 == "*"):
    ef = inp1 * inp3
    print("The Multiplication of: " , ef)
elif (inp2 == "/"):
    gh = inp1 / inp3
    print("The Division of: " , gh)
else:
    print("Invalid Option")