# While Loop

# Example 1: Simple Counter
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Example 2: While Loop (with break)
num = 1
while num <= 10:
    if num == 5:
        print("Breaking the loop at", num)
        break
    print("Current number:", num)
    num += 1

# Example 3: While Loop (with continue)
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print("Odd number:", num)

