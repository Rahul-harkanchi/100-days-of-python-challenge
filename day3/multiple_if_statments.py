print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill +=5
        print(f"Please pay ${bill}.")
    elif age <= 18:
        bill +=7
        print(f"Please pay ${bill}.")
    else:
        bill +=12
        print(f"Please pay ${bill}.")
    wants_photo = input("Would you like to take a photo? (Y/N) ")
    bill +=3
    if wants_photo == "y":
        print(f"your final bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
