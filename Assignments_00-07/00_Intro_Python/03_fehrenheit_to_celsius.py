fahrenheit = float(input("Enter temperature in Fahrenheit: "))

bold_italic = "\033[1;3m"
reset = "\033[0m"


celsius = (fahrenheit - 32) * 5.0 / 9.0

print(f"Temperature: {bold_italic}{fahrenheit}F = {celsius}C{reset}")
