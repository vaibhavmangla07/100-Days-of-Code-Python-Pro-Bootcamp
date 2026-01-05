# Creating a sample list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# 1. append() - Adds an element at the end
my_list.append(60)
print("append(60):", my_list)

# 2. extend() - Adds elements from another list
my_list.extend([70, 80])
print("extend([70, 80]):", my_list)

# 3. insert(index, element) - Inserts an element at a specific position
my_list.insert(2, 25)
print("insert(2, 25):", my_list)

# 4. remove(value) - Removes the first occurrence of a value
my_list.remove(25)
print("remove(25):", my_list)

# 5. pop() - Removes and returns the last element
last_element = my_list.pop()
print("pop():", last_element)
print("After pop:", my_list)

# 6. pop(index) - Removes and returns the element at a specific index
element_at_1 = my_list.pop(1)
print("pop(1):", element_at_1)
print("After pop(1):", my_list)

# 7. index(value) - Returns the index of the first occurrence of a value
index_30 = my_list.index(30)
print("index(30):", index_30)

# 8. count(value) - Returns the count of a value in the list
count_10 = my_list.count(10)
print("count(10):", count_10)

# 9. sort() - Sorts the list in ascending order
unsorted_list = [3, 1, 4, 2, 5]
unsorted_list.sort()
print("sort():", unsorted_list)

# 10. sort(reverse=True) - Sorts in descending order
unsorted_list.sort(reverse=True)
print("sort(reverse=True):", unsorted_list)

# 11. reverse() - Reverses the list in-place
unsorted_list.reverse()
print("reverse():", unsorted_list)

# 12. copy() - Returns a shallow copy of the list
copied_list = my_list.copy()
print("copy():", copied_list)

# 13. clear() - Removes all elements from the list
temp_list = [1, 2, 3]
temp_list.clear()
print("clear():", temp_list)

# 14. len() - Returns the length of the list
print("len(my_list):", len(my_list))

# 15. max() - Returns the maximum element
print("max(my_list):", max(my_list))

# 16. min() - Returns the minimum element
print("min(my_list):", min(my_list))

# 17. sum() - Returns the sum of all elements
print("sum(my_list):", sum(my_list))

# 18. list() - Converts an iterable (e.g., string) to a list
string_list = list("hello")
print("list('hello'):", string_list)

# 19. slicing - Accessing parts of the list
print("my_list[1:4]:", my_list[1:4])  # from index 1 to 3

# 20. list comprehension - Creating lists using conditions
squared_list = [x**2 for x in range(5)]
print("List comprehension (squares):", squared_list)

# 21. Membership test - Checking if an element exists
print("30 in my_list:", 30 in my_list)

# 22. Iteration over list
print("Iterating over my_list:")
for item in my_list:
    print(item, end=" ")
print()
