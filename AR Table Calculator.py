while(True):
    nums = int(input("Enter the Value of Table of you want"))
    for a in range(10):
        print(nums , "x" , a+1 , "=" , nums*(a+1))
    user = input("Enter Q to quit or other key to continue")
    if (user == "Q"):
        break