from datetime import date
import sys
import operator
import inflect

p = inflect.engine()

def main():
    try:
        birth = input("Date of birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(birth))
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid Date")


def convert(time):
    minutes = time * 24 * 60
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
