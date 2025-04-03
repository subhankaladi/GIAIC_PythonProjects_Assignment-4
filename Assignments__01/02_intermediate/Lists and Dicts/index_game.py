def access_element(my_list, index):
    """Returns the element at the given index or an error message."""
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    return "Index out of range!"

def modify_element(my_list, index, new_value):
    """Modifies the element at the given index or returns an error."""
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Updated list: {my_list}"
    return "Index out of range!"

def slice_list(my_list, start, end):
    """Returns a sliced list with proper index handling."""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return f"Sliced list: {my_list[start:end]}"
    return "Invalid indices!"

def main():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    
    while True:
        print("\nOperations: 1. Access  2. Modify  3. Slice  4. Exit")
        choice = input("Choose an operation: ")

        if choice == "1":
            index = int(input("Enter index: "))
            print(access_element(my_list, index))

        elif choice == "2":
            index = int(input("Enter index: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
