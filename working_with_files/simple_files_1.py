# Opening a file
file = open("test_data.txt", "r")

# Read all content
print(file.read())

# Read 1 line, move the cursor to the next one
print(file.readline())

# Read all the lines
print(file.readlines())


file.close()

# Using with notation: file is accessible
with open("test_data.txt", "r") as file:
    content = file.read
    print(content)


