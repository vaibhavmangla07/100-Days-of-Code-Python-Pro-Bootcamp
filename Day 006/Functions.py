# 1. Function with No Parameters and No Return
def myFunction():
    print("Hello! Welcome to Python functions.")
myFunction()


# 2. Function with Parameters
def add(a, b):
    print("Sum:", a + b)
add(5, 3)


# 3. Function with Return Value
def multiply(a, b):
    return a * b
result = multiply(4, 5)
print("Product:", result)


# 4. Function with Default Parameter
def welcome(name="User"):
    print(f"Hello {name}")
welcome("World!")
welcome()  # Uses default value

# 5. Function Returning Multiple Values
def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, prod = calculate(10, 5)
print("Sum:", sum_)
print("Difference:", diff)
print("Product:", prod)


# 6. Function Calling Another Function
def square(x):
    return x * x
def display_square(num):
    print("Square is:", square(num))

display_square(6)


# 7. Using `*args` to Accept Variable Number of Arguments
def total_sum(*numbers):
    return sum(numbers)

print("Total:", total_sum(1, 2, 3, 4, 5))
