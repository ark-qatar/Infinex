import random
list = []
b = input("Enter 1st value: ")
c = input("Enter 2nd value or press Enter to skip: ")
d = input("Enter 3rd value or press Enter to skip: ")
e = input("Enter 4th value or press Enter to skip: ")
f = input("Enter 5th value or press Enter to skip: ")
g = input("Enter 6th value or press Enter to skip: ")

if (b):
    list.append(b)
if (c):
    list.append(c)
if (d):
    list.append(d)
if (e):
    list.append(e)
if (f):
    list.append(f)
if (g):
    list.append(g)

if (list):
    h = random.choice(list)
    print("Random Value:", h)
else:
    print("No values to choose from.")