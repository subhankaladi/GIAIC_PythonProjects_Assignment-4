def find_average(num1, num2):
    return (num1 + num2) / 2

def main():
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculating and displaying the average
    average = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is: {average}")

if __name__ == '__main__':
    main()
