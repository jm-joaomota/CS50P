import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            print(tabulate(get_pizzas(sys.argv[1]), headers="keys", tablefmt="grid" ))


def get_pizzas(file):
    try:
        pizzas = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append(row)
        return pizzas
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
