import csv
import datetime

# Define the store name
store_name = "ShopSmart"

# Define the sales tax rate
sales_tax_rate = 0.06

# Get the current date and time
current_datetime = datetime.datetime.now()

# Check if today is Tuesday or Wednesday
if current_datetime.weekday() in [1, 2]:  # 1 = Tuesday, 2 = Wednesday
    discount_rate = 0.10
else:
    discount_rate = 0.00

try:
    # Read the products CSV file
    with open("C:/Users/moses/Desktop/Programming_with_Functions_CSE111/week05/products.csv", 0) as products_file:
        products_reader = csv.reader(products_file)
        next(products_reader)  # Skip the header row
        products = {row[0]: float(row[2]) * (1 - discount_rate) for row in products_reader}  # Apply discount

    # Read the request CSV file
    with open("C:/Users/moses/Desktop/Programming_with_Functions_CSE111/week05/request.csv", 'r') as request_file:
        request_reader = csv.reader(request_file)
        next(request_reader)  # Skip the header row
        request = {row[0]: int(row[1]) for row in request_reader}

    # Print the store name at the top of the receipt
    print(store_name)

    # Print the list of ordered items
    for product, quantity in request.items():
        price = products[product]
        print(f"{product}: {quantity} x ${price:.2f} = ${quantity * price:.2f}")

    # Sum and print the number of ordered items
    total_items = sum(request.values())
    print(f"Total items: {total_items}")

    # Sum and print the subtotal due
    subtotal = sum(quantity * products[product] for product, quantity in request.items())
    print(f"Subtotal: ${subtotal:.2f}")

    # Compute and print the sales tax amount
    sales_tax = subtotal * sales_tax_rate
    print(f"Sales tax: ${sales_tax:.2f}")

    # Compute and print the total amount due
    total_due = subtotal + sales_tax
    print(f"Total due: ${total_due:.2f}")

    # Print a thank you message
    print("Thank you for shopping at ShopSmart!")

    # Print the current date and time
    print(f"Date and time: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

except KeyError:
    print("Error: Product not found in catalog")
