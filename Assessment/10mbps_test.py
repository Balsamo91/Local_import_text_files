# Importing datatime module to keep track of event times for when the user do operations
import datetime
from import_functions import history, read_balance, write_balance, read_inventory, write_inventory

print("\nWelcome to the company's Account and Warehouse!\n")

# Setting up the global variable and empty list 
balance_file = "balance.txt"
inventory = "warehouse.txt"
history_file = "history.txt"
account = read_balance(balance_file)
warehouse_list = read_inventory(inventory)
operations_recorded = [] # In here I am recording every single oparation done by the user


# Start of the program
while True:
    # Asking the user to chose an option based on what they want to do
    print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
    action = input("What would you like to do?: ").lower()
    operations_recorded.append({
    "type": "choosing action",
    "action": action,
    "timestamp": datetime.datetime.now()})

    # If user type "end" the program terminates
    if action == "end":
        write_balance(balance_file, account)
        history(operations_recorded, history_file)
        break
    
    # If user type "balance" the program will ask user input and if not int() the user will need to restart
    elif action == "balance":
        try:
            balance = float(input("Enter the ammount you want to add or substract: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # Starts the validation and it will prevent the account to go negative
        while True:
            if account + balance >= 0:
                account += balance # this will add the balance to account
                operations_recorded.append({
                "type": "balance action",
                "account": balance,
                "timestamp": datetime.datetime.now()})
                history(operations_recorded, history_file)
                break
            # checking if the user subtract more than the ammount available
            elif account <= 0 and balance <= 0:
                print("\nNot sufficient funds! Retry another time!")
                break
            else:
                print("\nNot sufficient funds! Retry another time!")
                break
    # If the user type "purchase" the program will ask user inputs and if not int() the user will need to restart
    elif action == "purchase":    
        try:
            name = str(input("Enter the name of product: ")).lower()
            price = int(input("Enter the price of the product: "))
            quantity = int(input("Enter the quantity required: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue

        # If account is higher than the purchase price entered then add the variable into the warehouse_list[] as a dictionary
        if account > price:
            # If user enters the same item, this will catch it and it will add the quantity, if not it will add the dict to the list warehouse_list[] 
            item_exist = False
            for p in warehouse_list:
                if p["name"] == name:
                    p["quantity"] += quantity
                    item_exist = True
                    write_inventory(inventory, warehouse_list)
                    break
            if not item_exist:
                warehouse_list.append({"name" : name, "price" : price, "quantity" : quantity})
                write_inventory(inventory, warehouse_list)
            account -= price * quantity # substract the purchased items from the account

            print(f"\nPurchase has been successful! {quantity} unit(s) of {name} bought for a total of {price * quantity}.")
            operations_recorded.append({
            "type": "purchase action",
            "name": name,
            "price": price,
            "quantity": quantity,
            "timestamp": datetime.datetime.now()})
            history(operations_recorded, history_file)
            
        else:
            print("\nNot enough fund, Bruh!!!!")
    

    # If the user type "sale" the program will ask user inputs and if not int() the user will need to restart
    elif action == "sale":
        try:
            name = input("Enter the name of product: ").lower()
            price = int(input("Enter the price of the product: "))
            quantity = int(input("Enter the quantity required: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # in the for loop checking if the warehouse_list[] there is availability of the item(s) requested.
        #If the user wants to sale less quantity then the quantity is calculated and updates the warehouse_list[]
        for s in warehouse_list:
            if s["name"] == name and (s["price"] <= price or s["price"] >= price) and s["quantity"] >= quantity:
                s["quantity"] -= quantity
                account += price * quantity
                print(f"\nSale has been successful! {quantity} unit(s) of {name} sold for a total of {price * quantity}.")
                operations_recorded.append({
                "type": "sale action",
                "name": name,
                "price": price,
                "quantity": quantity,
                "timestamp": datetime.datetime.now()})
                history(operations_recorded, history_file) ###############################################################################
                write_inventory(inventory, warehouse_list)
                break
        else:
            print("\nProduct not found or insufficient quantity in the warehouse, Bruh!!!")

    # It gives to the ammount available
    elif action == "account":
        print(f"\nThe total ammount availble is € {account}!")
        operations_recorded.append({
        "type": "account action",
        "timestamp": datetime.datetime.now()})
        history(operations_recorded, history_file) ###############################################################################

    # It will print everything in the warehouse listing it nicely
    elif action == "list":
        print("\nThe warehouse availability is the following:\n")
        for list in warehouse_list:
            print()
            for key, value in list.items():
                print(f"- {key.capitalize()}: {value}")
                operations_recorded.append({
                "type": "list action",
                "timestamp": datetime.datetime.now()})
            history(operations_recorded, history_file) ###############################################################################

    # It will ask the user to input the name of the item. if not present it will say not present
    elif action == "warehouse":
        name = input("Enter the name of product: ")
        for find in warehouse_list:
            if find["name"] == name:
                print(f"\nHere is the result:\n\nName: {find['name']}\nQuantity: {find['quantity']}")
                operations_recorded.append({
                "type": "list action",
                "timestamp": datetime.datetime.now()})
                history(operations_recorded, history_file) ###############################################################################
                break
        else:
            print("\nProduct is not in the system, Bruh!!!")

    # It will ask the user to enter a digit or press enter.
    elif action == "review":
        try:
            from_indice_input = input("From when you want to start? (start from 1 as for the oldest in time)-(press Enter to skip): ")
            to_indice_input = input("To when you want to check data? (higher number means lastest data)-(press Enter to skip): ")
            
            # if Enter is pressed it will print all recored operations
            if from_indice_input == "" and to_indice_input == "":
                for no_input in operations_recorded:
                    print()
                    for key1, value1 in no_input.items():
                        print(f"- {key1.capitalize()}: {value1}")
            else:
                # if digits are entered then it convert the input to int() and if it is within range it will provide the info in range else it will say not in range
                from_indice = int(from_indice_input) if from_indice_input else 0
                to_indice = int(to_indice_input) if to_indice_input else len(operations_recorded)

                if 0 < from_indice <= len(operations_recorded) and 0 < to_indice <= len(operations_recorded) and from_indice <= to_indice:
                    for r in range(from_indice - 1, to_indice):
                        review = operations_recorded[r]
                        print()
                        for key1, value1 in review.items():
                            print(f"- {key1.capitalize()}: {value1}")
                else:
                    print("\nNot in range, Bruh!!!")

        except ValueError:
            print("\nInvalid input. Please enter valid indices.")

    else:
        print("\nInvalid command!\n")