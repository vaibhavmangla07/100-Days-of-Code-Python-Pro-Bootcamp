score = [150, 120, 23, 45, 67, 89, 105, 27, 55, 76, 93, 82, 11, 22, 69]

total = sum(score)
print("Total Sum :", total)

# Logic
sum = 0
for s in score:
    sum += s
print(sum)

print("Max Score :", max(score))

# Logic
maxScore = 0
for s in score:
    if s > maxScore:
        maxScore = s
print(maxScore)