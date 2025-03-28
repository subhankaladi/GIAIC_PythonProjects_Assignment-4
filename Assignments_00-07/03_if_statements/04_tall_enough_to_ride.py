def main():
    while True:
        # User se height input lena
        height = input("How tall are you? ")

        # Agar user ne khali enter press kiya to program stop ho jaye
        if height == "":
            print("Exiting the program. Have a great day!")
            break

        # Input ko number me convert karna
        height = int(height)

        # Height check karna
        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

# Yeh line program ko run karne ke liye zaroori hai
if __name__ == '__main__':
    main()
