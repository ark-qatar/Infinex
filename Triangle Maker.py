inp1 = int(input("Enter how many lines you want in your triangle: "))

for lines in range (1, inp1 + 1):
    print(" " * (inp1 - lines), end="")
    print("*" * (2 * lines - 1))