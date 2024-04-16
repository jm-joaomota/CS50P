def main():

    fraction = get_fra()

    x, y = fraction.split("/")
    x, y = int(x), int(y)

    percentage = (x / y) * 100

    if percentage <= 1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(round(percentage)) + "%"


def get_fra():

    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split("/"))

            if x <= 0 or y <= 0 or x > y:
                raise ValueError
            return fraction
        
        except ValueError:
            print("Write a valid fraction")
        except ZeroDivisionError:
            print("Invalid input. Y cannot be zero.")

if __name__ == '__main__':
    percentage = main()
    print(f"The tank is {percentage}")
