import random

friends = ["Roy", "Joy", "Alice", "Micheal", "James"]

# 1st Option
print(random.choice(friends))

# 2nd Option
randomIndex = random.randint(0, 4)
print(friends[randomIndex])