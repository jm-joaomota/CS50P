def calculate_energy(mass):
    #Speed of light in meters per second
    speed_of_light = 300000000

    # Energy (E) = mass (m) * speed of light (c) squared
    energy = mass * speed_of_light ** 2
    return energy

def main():
    # Prompt the user for mass in kilograms
    mass = int(input("Enter mass in kilograms: "))

    # Calculate Energy
    energy = calculate_energy(mass)

    # Output the equivalent energy in Joules
    print("Equivalent energy:", energy, "Joules")

main()

