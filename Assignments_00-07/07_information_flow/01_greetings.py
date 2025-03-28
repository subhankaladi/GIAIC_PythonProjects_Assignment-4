def greet(name):
    """Prints a greeting with the given name."""
    print(f"Greetings {name}!")

def main():
    # Ask the user for their name
    name = input("What's your name? ")
    
    # Call the greet function with the user's name
    greet(name)

# Required line to run the program
if __name__ == '__main__':
    main()
