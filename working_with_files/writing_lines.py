# Opening file
file = open("test.txt", "w")

# Writing into a file
file.write("Hello world")

line_to_write = ["\nFirst line", "\nSecond Line", "\nthird line"]

# Wrinting lines into file
file.writelines(line_to_write)

file.close()

# Using woth
with open("test.txt", "w") as file:
    file.writelines(line_to_write)
