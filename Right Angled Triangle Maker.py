inp1 = int(input("Enter in how many line you want your right angled triangle: "))
for lines in range(inp1):
    for stars in range(lines+1):
        print("*" , end = " ")
    print()