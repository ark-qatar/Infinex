import requests

# Ask user for direction
choice = input("Type 'PA.QA' for PKR to QAR or 'QA.PA' for QAR to PKR: ")
amount = float(input("Enter the amount: "))

# Get exchange rate
data = requests.get("https://open.er-api.com/v6/latest/QAR").json()
rate = data["rates"]["PKR"]

# Do the conversion
if choice == "QA.PA".upper():
    result = amount * rate
    print(f"{amount} QAR = {result} PKR")
elif choice == "PA.QA".upper():
    result = amount / rate
    print(f"{amount} PKR = {round(result, 4)} QAR")
else:
    print("Bro... that's not a valid option. Use 'PA.QA' or 'QA.PA'.")