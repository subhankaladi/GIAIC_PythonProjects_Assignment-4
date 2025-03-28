import random  # Random module import karna

def main():
    # 10 random numbers generate karna aur unko space-separated print karna
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(*random_numbers)

# Program ko run karne ke liye ye zaroori hai
if __name__ == '__main__':
    main()
