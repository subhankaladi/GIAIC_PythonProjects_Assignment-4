def main():
    # Ask the user for a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Loop until curr_value is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print the current value in the same line

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
