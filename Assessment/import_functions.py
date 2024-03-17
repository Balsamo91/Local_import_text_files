# for (balance) I need to OVERWRITE the amount saved in amount.txt

def read_balance(balance_file):
    try:
        with open(balance_file, "r") as file:
            return float(file.read())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

def write_balance(balance_file, account):
    try:
        with open(balance_file, "w") as file:
            file.write(str(account))
            file.close()
            print("\nBalance updated in balance file.\n")
    except Exception as e:
        print(f"\nError saving balance data: {e}")


# for (Warehouse) inventory I need to UPDATE/OVERWRITE the file warehouse.txt

def read_inventory(inventory_file):
    import json
    warehouse_list = []
    try:
        with open(inventory_file, "r") as file:
            for line in file:
                try:
                    # Convert each line to a dictionary using JSON parsing
                    item = json.loads(line)
                    warehouse_list.append(item)
                except json.JSONDecodeError as e:
                    print(f"Error decoding line '{line.strip()}': {e}")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"Error reading inventory data: {e}")
    return warehouse_list


def write_inventory(inventory, warehouse_list):
    import json
    try:
        with open(inventory, "w") as file:
            for item in warehouse_list:
                # Write each dictionary as a JSON string on a separate line
                file.write(json.dumps(item) + '\n')
        print("Inventory updated in warehouse file.\n")
    except Exception as e:
        print(f"Error saving inventory: {e}")


# for (history) operations I need to APPEND every operations

def history(operations_recorded, history_file):

    try:
        with open(history_file, "a") as file:
            for h in operations_recorded:
                file.write(str(h) + "\n")
            file.close()
    except Exception as e:
        print(f"Error saving history: {e}")

