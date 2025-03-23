def get_first_element(lst):
    """ Prints the first element of a given non-empty list. """
    print("The first element in the list is:", lst[0])

def main():

    n = int(input("Enter the number of elements in the list: "))
    lst = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)  


    get_first_element(lst)

# Required line to run the program
if __name__ == '__main__':
    main()
