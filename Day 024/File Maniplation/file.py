# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# for reading
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    # file.close()

# For Writing (Remove old and write new)
with open("my_file.txt", mode="w") as file:
    file.write("New Text.")

# For Appending the data
with open("my_file.txt", mode="a") as file:
    file.write("\nData Scientist")
    print(contents)
