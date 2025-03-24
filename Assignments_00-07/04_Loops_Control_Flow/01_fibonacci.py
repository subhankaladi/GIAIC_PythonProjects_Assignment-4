def main():
    MAX_VALUE = 10000  # Constant value

    # Starting values of Fibonacci sequence
    a, b = 0, 1
    
    # Print Fibonacci numbers until we reach MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=" ")  # Print number with space
        a, b = b, a + b  

# Required to call the main function
if __name__ == '__main__':
    main()
