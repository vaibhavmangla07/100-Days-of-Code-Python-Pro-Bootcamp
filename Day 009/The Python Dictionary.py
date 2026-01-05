# Example 1: Creating and Accessing a Dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

print(student["name"])
print(student.get("age"))

print(student.get("grade", "Not found"))
print("\n")


# Example 2: Modifying a Dictionary
car = {"brand": "Toyota", "model": "Camry", "year": 2018}

car["color"] = "Blue"
car["year"] = 2020
del car["model"]

print(car)
print("\n")


# Example 3: Iterating Over a Dictionary
scores = {"math": 95, "science": 88, "history": 92}

for subject in scores:
    print(subject)

for subject, score in scores.items():
    print(f"{subject}: {score}")
print("\n")


# Example 4: Dictionary Methods
inventory = {"apples": 10, "bananas": 20, "oranges": 15}

print(inventory.keys())
print(inventory.values())
print(inventory.items())

bananas = inventory.pop("bananas")
print(bananas)
print(inventory)

inventory.clear()
print(inventory)
print("\n")


# Example 5: Nested Dictionaries
university = {
    "student1": {"name": "Bob", "age": 21, "grades": [85, 90, 88]},
    "student2": {"name": "Clara", "age": 22, "grades": [92, 87, 95]}
}

print(university["student1"]["name"])
print(university["student2"]["grades"][0])

university["student1"]["grades"].append(91)
print(university["student1"]["grades"])
print("\n")


# Example 6: Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)

evens = {k: v for k, v in squares.items() if v % 2 == 0}
print(evens)
print("\n")
