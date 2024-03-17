
# def balance():
#     try:
#         with open("balance.txt", "r") as file:
#             return float(file.read())
#     except (FileNotFoundError, ValueError):
#         return 0

# def balance_w(account):
#     with open("balance.txt", "w") as file:
#         file.write(str(account))




# def balance_read(balance_file):
#     try:
#         with open(balance_file, 'r') as file:
#             return float(file.read())
#     except FileNotFoundError:
#         print("Balance file not found. Starting with zero balance.")
#         return 0
#     except ValueError:
#         print("Error reading balance data. Starting with zero balance.")
#         return 0








# def balance():
#     # Read balance from file
#     account = balance_r()

#     # Display current balance to the user
#     print(f"Current balance: {account}")
    
#     # Ask user for input to add or subtract balance
#     while True:
#         try:
#             balance_change = float(input("Enter the amount to add or subtract (positive for addition, negative for subtraction): "))
#             break
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
    
#     # Update balance based on user input
#     account += balance_change
    
#     # Record the balance operation with timestamp
#     operation = {
#         "type": "balance",
#         "amount": balance_change,
#         "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
#     record_operation(operation)
    
#     # Write updated balance to file
#     balance_w(account)

#     print("Balance updated successfully.")

# def balance_r():
#     try:
#         with open("balance.txt", "r") as file:
#             return float(file.read())
#     except (FileNotFoundError, ValueError):
#         return 0

# def balance_w(account):
#     with open("balance.txt", "w") as file:
#         file.write(str(account))


# def balance_w(account):
#     with open("balance.txt", "w") as file:
#         # Write updated balance to file
#         file.write(str(account))
    
#     print("Balance updated successfully.")

# def record_operation(operation):
#     # Append operation to a file for history
#     with open("operations_history.txt", "a") as file:
#         file.write(f"{operation}\n")

# # Example usage
# balance()


# def history(operations_recorded, filename):
#     try:
#         filename = open('history.txt', 'w')
#         filename.write(str(operations_recorded) + "\n")
#         print("Operations recorded successfully!")
#         filename.close()

#     except Exception as e:
#         print(f"Error saving history: {e}")
        
# def read_inventory(inventory):
#     try:
#         with open(inventory, "r") as file:
#             return file.read()
#     except FileNotFoundError:
#         return inventory
    
# def read_inventory(inventory):
#     import json
#     warehouse_list = []
#     try:
#         with open(inventory, "r") as file:
#             for line in file:
#                 data = json.loads(line)
#                 warehouse_list.append(data)
#     except FileNotFoundError:
#         print("Inventory file not found.")
#     except json.JSONDecodeError:
#         print("Error decoding inventory data.")
#     return warehouse_list

# # def write_inventory(inventory, warehouse_list):
# #     try:
# #         with open(inventory, "a") as file:
# #             file.write(str(warehouse_list))
# #             file.close()
# #             print("\inventory updated in warehouse file.\n")
# #     except Exception as e:
# #         print(f"Error saving inventory: {e}")


# def write_inventory(inventory, warehouse_list):
#     import json
#     try:
#         with open(inventory, "w") as file:
#             for items in warehouse_list:
#                 file.write(json.dumps(items) + '\n')
#                 file.close()
#         print("Inventory updated in warehouse file.\n")
#     except Exception as e:
#         print(f"Error saving inventory: {e}")

# def read_inventory(inventory):
#     warehouse_list = []
#     try:
#         with open(inventory, "r") as file:
#             for line in file:
#                 # Convert each line (assumed to be JSON string representing a dictionary) to a dictionary
#                 item = eval(line)
#                 warehouse_list.append(item)
#     except FileNotFoundError:
#         print("Inventory file not found.")
#     except Exception as e:
#         print(f"Error reading inventory data: {e}")
#     return warehouse_list

# def write_inventory(inventory, warehouse_list):
#     try:
#         with open(inventory, "w") as file:
#             for item in warehouse_list:
#                 # Write each item in warehouse_list as a string representation of a dictionary (JSON-like)
#                 file.write(str(item) + '\n')
#         print("Inventory updated in warehouse file.\n")
#     except Exception as e:
#         print(f"Error saving inventory: {e}")

# def read_inventory(inventory):
#     import json
#     warehouse_list = []
#     try:
#         with open(inventory, "r") as file:
#             for line in file:
#                 # Convert each line to a dictionary using JSON parsing
#                 item = json.loads(line)
#                 warehouse_list.append(item)
#     except FileNotFoundError:
#         print("Inventory file not found.")
#     except json.JSONDecodeError as e:
#         print(f"Error decoding inventory data: {e}")
#     return warehouse_list
