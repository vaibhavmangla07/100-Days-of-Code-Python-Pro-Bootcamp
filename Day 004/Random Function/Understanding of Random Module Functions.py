import random

# 1. random() - Returns a random float number between 0.0 and 1.0
print("random():", random.random())

# 2. uniform(a, b) - Returns a random float number between a and b
print("uniform(10, 20):", random.uniform(10, 20))

# 3. randint(a, b) - Returns a random integer between a and b (inclusive)
print("randint(1, 10):", random.randint(1, 10))

# 4. randrange(start, stop[, step]) - Returns a random number from range(start, stop, step)
print("randrange(0, 100, 5):", random.randrange(0, 100, 5))

# 5. choice(seq) - Returns a randomly selected element from a non-empty sequence
print("choice(['apple', 'banana', 'cherry']):", random.choice(['apple', 'banana', 'cherry']))

# 6. choices(population, weights=None, k=1) - Returns a list of k elements chosen with replacement
print("choices(['a', 'b', 'c'], k=2):", random.choices(['a', 'b', 'c'], k=2))

# 7. sample(population, k) - Returns a list of k unique elements chosen without replacement
print("sample(range(100), 5):", random.sample(range(100), 5))

# 8. shuffle(x) - Shuffles the sequence in place (modifies the original list)
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("shuffle([1, 2, 3, 4, 5]):", my_list)

# 9. seed(a=None) - Initializes the random number generator (useful for reproducibility)
random.seed(42)
print("random() with seed 42:", random.random())  # Same output every time

# 10. betavariate(alpha, beta) - Beta distribution
print("betavariate(2.0, 5.0):", random.betavariate(2.0, 5.0))

# 11. expovariate(lambd) - Exponential distribution
print("expovariate(1.5):", random.expovariate(1.5))

# 12. gammavariate(alpha, beta) - Gamma distribution
print("gammavariate(2.0, 2.0):", random.gammavariate(2.0, 2.0))

# 13. gauss(mu, sigma) - Gaussian distribution
print("gauss(0, 1):", random.gauss(0, 1))

# 14. lognormvariate(mu, sigma) - Log-normal distribution
print("lognormvariate(0, 1):", random.lognormvariate(0, 1))

# 15. normalvariate(mu, sigma) - Normal distribution
print("normalvariate(0, 1):", random.normalvariate(0, 1))

# 16. triangular(low, high, mode) - Triangular distribution
print("triangular(1, 10, 5):", random.triangular(1, 10, 5))

# 17. vonmisesvariate(mu, kappa) - Circular data distribution
print("vonmisesvariate(0, 4):", random.vonmisesvariate(0, 4))

# 18. weibullvariate(alpha, beta) - Weibull distribution
print("weibullvariate(1.0, 1.5):", random.weibullvariate(1.0, 1.5))
