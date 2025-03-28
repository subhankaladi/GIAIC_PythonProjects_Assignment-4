# Define the adult age (for the USA)
ADULT_AGE = 18  

def is_adult(age):
    """Returns True if the age is 18 or older, otherwise returns False."""
    return age >= ADULT_AGE  

def main():
    # Ask the user for their age
    age = int(input("How old is this person?: "))
    
    # Call is_adult() function and print the result
    print(is_adult(age))

# Required line to run the program
if __name__ == '__main__':
    main()
