def main():
    num1: int = int(input("\033[1;3mPlease enter an integer to be divided:\033[0m "))  
    num2: int = int(input("\033[1;3mPlease enter an integer to divide by:\033[0m "))  

    quotient: int = num1 // num2
    remainder: int = num1 % num2

    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
