#Tip calculator

print("Welcome to the tip calculator.\n")

BillTotal = float(input("What was the total bill?\n$"))

PeopleInParty = int(input("How many people are splitting the bill?\n"))

TipPercentage = float(input("What percent do you want to tip?\n"))

TipAmount = (BillTotal * (TipPercentage/100))

FinalBill = round((TipAmount + BillTotal)/PeopleInParty,2)
print(f"To tip {TipPercentage}% ontop of the bill, each person should pay: ${FinalBill}")