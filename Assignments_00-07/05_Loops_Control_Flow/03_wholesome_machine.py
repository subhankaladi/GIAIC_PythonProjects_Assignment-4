def main():
    affirmation = "I am capable of doing anything I put my mind to."
    print(f"Please type the following affirmation: {affirmation}")

    while True:
        user_input = input("\033[34m")  # This makes user input appear in blue
        print("\033[0m", end="")  # Resets color back to normal

        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation. Please type the following affirmation:", affirmation)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
