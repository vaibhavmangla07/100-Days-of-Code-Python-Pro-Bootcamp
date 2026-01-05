height = 1.75
weight = 84

bmi = weight / height ** 2
print(bmi)

print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

# F-string
score = 0
height = 1.75
win = True
print(f"Score : {score}, Height : {height}, Winning : {win}")