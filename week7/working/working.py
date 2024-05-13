import re


def main():
    convert(input("Hours: "))


def convert(s):
    if matches := re.search(
        r"^([1-9]|1[0-2]):([0-5][0-9]) AM to ([1-9]|1[0-2]):([0-5][0-9]) (?:PM)$", s
    ):
        am = int(matches.group(1)) if int(matches.group(1)) != 12 else 0
        pm = int(matches.group(3)) + 12
        print(f"{am}:{matches.group(2)} to {pm}:{matches.group(4)}")
    elif matches := re.search(r"^([1-9]|1[0-2]) AM to ([1-9]|1[0-2]) (?:PM)$", s):
        am = int(matches.group(1)) if int(matches.group(1)) != 12 else 0
        pm = int(matches.group(2)) + 12
        print(f"{am}:00 to {pm}:00")
    elif matches := re.search(
        r"^([1-9]|1[0-2]):([0-5][0-9]) PM to ([1-9]|1[0-2]):([0-5][0-9]) (?:AM)$", s
    ):
        am = int(matches.group(3)) if int(matches.group(3)) != 12 else 0
        pm = int(matches.group(1)) + 12
        print(f"{pm}:{matches.group(2)} to {am}:{matches.group(4)}")
    elif matches := re.search(r"^([1-9]|1[0-2]) PM to ([1-9]|1[0-2]) (?:AM)$", s):
        am = int(matches.group(2)) if int(matches.group(1)) != 12 else 0
        pm = int(matches.group(1)) + 12
        print(f"{pm}:00 to {am}:00")
    else:
        raise ValueError


if __name__ == "__main__":
    main()
