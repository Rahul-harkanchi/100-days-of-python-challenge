print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = tip / 100
tip_final = bill * tip
final_bill = tip_final + bill
split_bill = final_bill / people
split_bill = round(split_bill, 2)

print(f"Each person should pay: $ {split_bill}")
