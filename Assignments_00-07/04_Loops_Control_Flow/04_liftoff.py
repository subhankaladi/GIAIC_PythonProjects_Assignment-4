def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):  # Starts from 10, goes to 1, decrementing by -1
        print(i, end=" ")  # Print numbers in the same line with space
    print("Liftoff!")  # Print Liftoff! at the end

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
