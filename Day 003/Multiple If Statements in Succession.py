print("Welcome to RollerCoaster!")
height = int(input("What is your height in cm ? "))

if (height > 120):
    print("You can Ride!")
    age = int(input("Enter age : "))
    if(age <= 12):
        bill = 5
        print("Pay 5$")
    elif(age <= 18):
        bill = 7
        print("Pay 7$")
    else:
        bill = 12
        print("Pay 12$")
    photos = input("Want Photos press y for yes or n for no : ")
    if(photos == "y"):
        bill += 3
    print(f"Your Total Bill is : {bill}$")
else:
    print("You can't Ride!")
