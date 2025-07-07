# Cube Calculator
inp1 = float(input("Enter the Length of your Figure: "))
inp2 = float(input("Enter the Width of your Figure: "))
inp3 = float(input("Enter the Height of your Figure: "))
var1 = inp1*inp2*inp3
if (inp1 == inp2 == inp3):
    print("Volume of the Cube: " , var1)
    print("It is a Cube")
else:
    print("Volume of the Cube: " , var1)
    print("It is a 3D Dimensional Cube")