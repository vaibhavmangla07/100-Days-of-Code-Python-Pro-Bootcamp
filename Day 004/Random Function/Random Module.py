import random
import myModule

randomInteger = random.randint(1, 10)
print(randomInteger)

print(myModule.myFavNumber)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

# Task to generate a head tail randomly
toss = random.randint(0, 1)
if toss == 0:
    print("Head")
else:
    print("Tail")