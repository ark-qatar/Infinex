inp1 = int(input("Enter in how many line you want your upside down triangle: "))
for lines in range(inp1):
    for stars in range(inp1 - lines):
        print("*" , end = " ")
    print()