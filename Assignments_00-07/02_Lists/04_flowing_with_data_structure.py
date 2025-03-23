def add_three_copies(my_list, data):
    """ Adds three copies of data to the given list (mutable behavior). """
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    # User input
    message = input("Enter a message to copy: ")

    # Empty list before modification
    my_list = []
    print("List before:", my_list)

    # Call the function (list changes without returning)
    add_three_copies(my_list, message)

    # List after modification
    print("List after:", my_list)

# Required line to run the program
if __name__ == '__main__':
    main()
