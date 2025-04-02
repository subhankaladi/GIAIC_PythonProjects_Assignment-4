def main():
    # Loop 10 se 1 tak count karne ke liye
    for i in range(10, 0, -1):  # 10 se 1 tak reverse countdown
        print(i, end=" ")  # Ek hi line me print karna
    
    # Jab countdown khatam ho, tab 'Liftoff!' print karna
    print("Liftoff!")

# Main function ko call karna
if __name__ == '__main__':
    main()
