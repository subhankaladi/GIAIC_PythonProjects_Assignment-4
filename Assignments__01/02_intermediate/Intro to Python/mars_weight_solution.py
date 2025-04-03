def main():
    # Dictionary to store planet gravity factors
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Taking user input
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    # Checking if planet is valid and calculating weight
    if planet in planet_gravity:
        planet_weight = round(earth_weight * planet_gravity[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")

# Ensuring main() runs when script is executed
if __name__ == "__main__":
    main()
