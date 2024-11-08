import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a dictionary and return the dictionary.
    Parameters:
    filename: the name of the CSV file to read.
    Return: a dictionary that contains the contents of the CSV file."""
    student_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line (headings)
        for row in reader:
            student_dict[row[0].replace('-', '')] = row[1]  # Remove dashes from I-Number
    return student_dict

def main():
    student_dict = read_dictionary('students.csv')
    while True:
        i_number = input("Enter an I-Number (or 'quit' to exit): ")
        if i_number.lower() == 'quit':
            break
        if len(i_number.replace('-', '')) != 9 or not i_number.replace('-', '').isdigit():
            print("Invalid I-Number")
        elif i_number.replace('-', '') in student_dict:
            print(student_dict[i_number.replace('-', '')])
        else:
            print("No such student")

if __name__ == "__main__":
    main()