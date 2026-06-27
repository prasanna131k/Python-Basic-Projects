

inventory = {}
transactions = []

def add_product():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Unit Price: "))
    qty = int(input("Enter Quantity: "))
    reorder = int(input("Enter Reorder Level: "))

    inventory[pid] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": qty,
        "reorder": reorder
    }

    print("Product Added Successfully!")

def stock_in():
    pid = input("Enter Product ID: ")

    if pid not in inventory:
        print("Product not found!")
        return

    qty = int(input("Enter Quantity to Add: "))
    inventory[pid]["quantity"] += qty

    transactions.append(f"IN - {pid} - {qty}")
    print("Stock Updated!")

def stock_out():
    pid = input("Enter Product ID: ")

    if pid not in inventory:
        print("Product not found!")
        return

    qty = int(input("Enter Quantity to Remove: "))

    if inventory[pid]["quantity"] >= qty:
        inventory[pid]["quantity"] -= qty
        transactions.append(f"OUT - {pid} - {qty}")
        print("Stock Removed!")
    else:
        print("Insufficient Stock!")

def view_inventory():
    print("\n----- INVENTORY -----")

    if not inventory:
        print("No Products Available")
        return

    print("ID\tName\tCategory\tPrice\tQty")

    for pid, data in inventory.items():
        print(
            pid,
            data["name"],
            data["category"],
            data["price"],
            data["quantity"],
            sep="\t"
        )

def low_stock_alert():
    print("\n----- LOW STOCK PRODUCTS -----")

    found = False

    for pid, data in inventory.items():
        if data["quantity"] <= data["reorder"]:
            print(pid, "-", data["name"])
            found = True

    if not found:
        print("No Low Stock Products")

def generate_report():
    total_products = len(inventory)

    total_value = 0
    categories = set()

    highest_product = None
    highest_value = 0

    for pid, data in inventory.items():
        value = data["price"] * data["quantity"]
        total_value += value

        categories.add(data["category"])

        if value > highest_value:
            highest_value = value
            highest_product = data["name"]

    print("\n===== INVENTORY REPORT =====")
    print("Total Products:", total_products)
    print("Total Stock Value:", total_value)
    print("Categories:", ", ".join(categories))

    if highest_product:
        print("Highest Value Product:", highest_product)

    low_count = 0
    for data in inventory.values():
        if data["quantity"] <= data["reorder"]:
            low_count += 1

    print("Low Stock Items:", low_count)

def save_inventory():
    file = open("inventory.txt", "w")

    for pid, data in inventory.items():
        file.write(
            f"{pid},{data['name']},{data['category']},{data['price']},{data['quantity']},{data['reorder']}\n"
        )

    file.close()

def load_inventory():
    try:
        file = open("inventory.txt", "r")

        for line in file:
            pid, name, category, price, qty, reorder = line.strip().split(",")

            inventory[pid] = {
                "name": name,
                "category": category,
                "price": float(price),
                "quantity": int(qty),
                "reorder": int(reorder)
            }

        file.close()

    except FileNotFoundError:
        pass

load_inventory()

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        stock_in()

    elif choice == "3":
        stock_out()

    elif choice == "4":
        view_inventory()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        generate_report()

    elif choice == "7":
        save_inventory()
        print("Data Saved. Exiting...")
        break

    else:
        print("Invalid Choice!")

