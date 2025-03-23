MAX_LENGTH = 3  # Define the maximum allowed length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Jab tak list ka size MAX_LENGTH se bada hai
        removed_item = lst.pop()  # Last element remove karo
        print("Removed:", removed_item)  # Remove kiya hua item print karo

def main():
    lst = []  #
    
    # User se list input lena
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("Original list:", lst)  # Pehli list print karo
    shorten(lst)  # shorten function ko call karo
    print("Shortened list:", lst)  # Final list print karo


if __name__ == '__main__':
    main()