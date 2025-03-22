animal = input("What's your favorite animal? ")

bold_italic = "\033[1;3m"
reset = "\033[0m"

print(f"My favorite animal is also {bold_italic}{animal}{reset}!")
