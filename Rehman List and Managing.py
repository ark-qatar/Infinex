import random

friends_list = []
copy_friends = []

print("1. Create an empty list")
print("2. Take input a new value name from the user.")
print("3. Take input a name from the user and delete it.")
print("4. Take input a name from the user and find out its index number.")
print("5. Create a copy of the list.")
print("6. Sort the list in descending order.")
print("7. Print the friends list.")
print("8. Print the copied list.")
print("9. Get a random value from your list.")
print("10. Quit")

while True:
    option = int(input("Enter the option 1 - 10: "))
    
    if (option == 1):
        friends_list.clear()
        print("List:", friends_list)

    elif (option == 2):
        new_name = input("Enter a new friend's name: ")
        friends_list.append(new_name)
        print("List:", friends_list)

    elif (option == 3):
        name = input("Enter a name to delete: ")
        if name in friends_list:
            friends_list.remove(name)
            print("List:", friends_list)
        else:
            print("Value not found!")
            print("List:", friends_list)

    elif option == 4:
        name = input("Enter a name to find its index number: ")
        if name in friends_list:
            i = friends_list.index(name)
            print("Index No:", i)
        else:
            print("Value not found!")

    elif option == 5:
        copy_friends = friends_list.copy()
        print("Copied List:", copy_friends)

    elif (option == 6):
        friends_list.sort(reverse=True)
        print("List:", friends_list)

    elif (option == 7):
        print("List:", friends_list)

    elif (option == 8):
        print("Copied List:", copy_friends)

    elif (option == 9):
        if (friends_list):
            a = random.choice(friends_list)
            print("Random Value:", a)
        else:
            print("List is empty.")

    elif (option == 10):
        print("Goodbye!")
        break

    else:
        print("Invalid Option. Please enter a number between 1 and 10.")