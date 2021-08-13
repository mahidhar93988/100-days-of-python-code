# roler coaster ride
print("Welcome to the ride")
height = int(input("Your height: "))
age = int(input("Your age: "))
bill = 0

if height >= 120:
    print("Yes you can ride")
    if age >= 12:
        bill = 5
        print("your bill is 7$, Thank you")

    elif age >= 18:
        bill = 10
        print("Yoyr bill is 10$, Thank you")
    elif age >= 45 and age <= 55:
        print("The ride is on us, and everythings gonna be fine")
    else:
        bill = 12
        print("Adult tickets are 12")

    want_photo = input("Do you want a photo: Y or N : ")
    if want_photo == "Y":

        bill += 3

    print(f"your final bill {bill}$")

else:
    print("Sorry, You need more height")
