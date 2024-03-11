from ast import literal_eval

user_input = input("Provide data: ")

data = literal_eval(user_input)

print(f"\nThis is the data: {data}")
print(f"Data type: {type(data)}")

