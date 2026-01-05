def myFun():
    print("Hello!")
    print("How are you")
    print("How's the weather today")

myFun()

# Function that allows inputs
def myFun_with_name(name):
    print(f"Hello! {name}")
    print(f"How are you {name}")

myFun_with_name("Vaibhav")

# Function with more than 1 input
def myFunction(name, location):
    print(f"Hello!, How are you {name}")
    print(f"Where you belongs to {location}")

myFunction("Vaibhav", "Punjab")
myFunction(name= "Vaibhav", location= "Punjab")

