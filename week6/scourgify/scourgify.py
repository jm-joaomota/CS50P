import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            files(sys.argv[1], sys.argv)


def files(input, output):
    try:
        with open(sys.argv[1]) as input:
            reader = csv.DictReader(input)
            with open("after.csv", "w") as output:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames=header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(",")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
