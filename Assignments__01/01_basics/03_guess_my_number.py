import random  # Random number generate karne ke liye

def main():
    # 0 se 99 ke beech ek random number choose karna
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # User se number input lena
        guess = int(input("Enter a guess: "))

        # Conditions check karna
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Correct answer milne par loop end kar dena

# Main function ko call karna
if __name__ == '__main__':
    main()
