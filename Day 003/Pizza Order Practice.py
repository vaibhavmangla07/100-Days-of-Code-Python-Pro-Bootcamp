print("Welcome to the Python Pizza Deliveries")
size = input("Enter size (S, M OR L) : ")
pepperoni = input("Do You want Pepperoni (Y or N) : ")
extraCheese = input("Do you want extra chesse (Y OR N) : ")

#todo : work out how much they need to pay based on size
bill = 0
if(size == "S"):
    bill += 15
elif(size == "M"):
    bill += 20
elif(size == "L"):
    bill += 25
else:
    print("Wrong Input!")

#todo : based on pepperoni
if(pepperoni == "Y"):
    if(size == "S"):
        bill += 2
    elif(size == "M"):
        bill += 3
    else:
        bill += 4

# todo : based on cheese and then total

if(extraCheese == "Y"):
    bill += 1

print(f"Total Bill : {bill}$Y")