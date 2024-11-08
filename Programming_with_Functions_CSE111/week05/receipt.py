import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    
    Parameters:
    filename (str): the name of the CSV file to read.
    key_column_index (int): the index of the column to use as the keys in the dictionary.
    
    Return:
    dict: a compound dictionary that contains the contents of the CSV file.
    """
    
    products_dict = {}
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            products_dict[key] = {'name': row[1], 'price': row[2]}
    
    return products_dict

def main():
    products_dict = read_dictionary("C:/Users/moses/Desktop/Programming_with_Functions_CSE111/week05/products.csv", 0)
    print(products_dict)
    with open("C:/Users/moses/Desktop/Programming_with_Functions_CSE111/week05/request.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line (column headings)
        for row in reader:
            product_number = row[0]
            requested_quantity = int(row[1])
            product_info = products_dict.get(product_number, None)
            if product_info:
                product_name = product_info['name']
                product_price = float(product_info['price'])
                print(f"Product Name: {product_name}, Requested Quantity: {requested_quantity}, Product Price: {product_price}")
            else:
                print(f"Product {product_number} not found")

if __name__ == "__main__":
    main()