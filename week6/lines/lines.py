import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            print(test_count_lines(sys.argv[1]))


def test_count_lines(file):
    try:
        count = 0
        with open(file, "r") as f:
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
