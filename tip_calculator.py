# Tip caliculator

bill = float(input("What is the total bill:"))
tip = int(input("How much tip would you like to give- 10,12,15:"))
people = int(input("How many people:"))
tip_percent = tip/100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay:${final_amount} ")
