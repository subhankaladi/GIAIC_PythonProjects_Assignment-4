def subtract_seven(num):
    return num - 7  # Subtracts 7 from the given number

def main():
    number = int(input("Enter a number: "))  # Get user input
    result = subtract_seven(number)  # Call the helper function
    print("Result after subtracting 7:", result)  # Print the result

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
