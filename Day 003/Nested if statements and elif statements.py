print("Welcome to RollerCoaster!")
height = int(input("What is your height in cm ? "))

if (height > 120):
    print("You can Ride!")
    age = int(input("Enter age : "))
    if(age <= 12):
        print("Pay 5$")
    elif(age <= 18):
        print("Pay 7$")
    else:
        print("Pay 12$")
else:
    print("You can't Ride!")
