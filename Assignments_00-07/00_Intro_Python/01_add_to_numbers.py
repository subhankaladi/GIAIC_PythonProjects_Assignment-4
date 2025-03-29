def main():
    
    num1 = input("\033[1;3m Enter the first number: \033[0m")
    
    num1 = int(num1)

    num2 = input("\033[1;3m Enter the second number: \033[0m")
    
    num2 = int(num2)
    
    total_sum = num1 + num2
    
    print("The total sum is:", total_sum)

if __name__ == "__main__":
    main()
