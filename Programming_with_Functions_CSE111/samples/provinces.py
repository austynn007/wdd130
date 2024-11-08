def modify_provinces():
    # Open the provinces.txt file for reading
    with open('provinces.txt', 'r') as file:
        # Read the contents of the file into a list
        provinces = file.read().splitlines()

    # Print the entire list
    print("Original list:")
    print(provinces)

    # Remove the first element from the list
    provinces.pop(0)

    # Remove the last element from the list
    provinces.pop()

    # Replace all occurrences of "AB" in the list with "Alberta"
    provinces = [province.replace("AB", "Alberta") for province in provinces]

    # Count the number of elements that are "Alberta" and print that number
    count = provinces.count("Alberta")
    print(f"Number of 'Alberta' elements: {count}")

    # Print the modified list
    print("Modified list:")
    print(provinces)

if __name__ == "__main__":
    modify_provinces()
