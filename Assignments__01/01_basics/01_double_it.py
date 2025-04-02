def main():
    # User se ek number input lena
    curr_value = int(input("Enter a number: "))  
    
    # Jab tak value 100 se choti hai, tab tak loop chalega
    while curr_value < 100:
        curr_value = curr_value * 2  # Value ka double karna
        print(curr_value, end=" ")  # Print karna (ek hi line me output dikhane ke liye)

# Main function ko call karna
if __name__ == '__main__':
    main()
