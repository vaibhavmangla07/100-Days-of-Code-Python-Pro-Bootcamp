# Example: Logical Operators (AND, OR, NOT) with generic variables
a, b, c = True, False, True

# AND: Both conditions must be True
if a and c:
    print("Both a and c are True (AND condition).")

# OR: At least one condition must be True
if b or c:
    print("Either b or c is True (OR condition).")

# NOT: Reverses the condition
if not b:
    print("b is False (NOT condition).")


# Example 2
# Logical Operators in Python

a = 10
b = 20

# 'and' operator
if a > 5 and b > 15:
    print("\nBoth conditions are True")  # This will execute

# 'or' operator
if a < 5 or b > 15:
    print("At least one condition is True")  # This will also execute

# 'not' operator
if not (a > b):
    print("a is not greater than b")  # True because a is not greater than b
