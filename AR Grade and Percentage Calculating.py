# Marks and Percentage
print("Total Marks is 200")
marks = int(input("Enter your Marks: "))
per1 = marks*100/200
print (per1)
if (per1 > 90):
	print("Congrats you got A+")
elif (per1 > 80):
	print("Nice! You got A Grade")
elif (per1 > 70):
	print("You got B+ grade but need some improvement")
elif (per1 > 60):
	print("You got B- grade and you should have to take extra classes")
elif (per1 > 50):
	print("You got C+ grade and you should come to your school with parents!!!!!")
elif (per1 > 40):
	print("You got C- grade and bring your parents to the school for a warni g letter")
elif (per1 < 40):
		print("You got Failed and you have repeat the same class again and bring your parents for the suspension letter!!!")
else:
		print("Invalid Grade")