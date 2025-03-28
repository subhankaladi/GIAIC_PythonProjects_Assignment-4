def count_even():
    lst = []  # Initialize an empty list
    
    # Taking input until the user presses Enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":  # Stop if Enter is pressed
            break
        
        try:
            num = int(user_input)  # Convert input to integer
            lst.append(num)  # Add to list
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Count even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    
    # Print the result
    print(f"Number of even numbers: {even_count}")

def main():
    count_even()

if __name__ == '__main__':
    main()
