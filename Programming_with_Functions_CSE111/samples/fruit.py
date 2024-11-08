def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # Add code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append("orange")
    print(f"after append: {fruit_list}")

    # Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    index = fruit_list.index("apple")
    fruit_list.insert(index, "cherry")
    print(f"after insert: {fruit_list}")

    # Add code to remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"after remove: {fruit_list}")

    # Add code to pop the last element from fruit_list and print the popped element and the list.
    last_element = fruit_list.pop()
    print(f"popped: {last_element}")
    print(f"after pop: {fruit_list}")

    # Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    # Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

# Call the main function
if __name__ == "__main__":
    main()