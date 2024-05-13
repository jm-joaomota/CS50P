import re


def main():
    count(input("Text: "))


def count(s):
    match = re.findall(r"(^|\W)um($|\W)", s, re.IGNORECASE)
    if match:
        print(len(match))


if __name__ == "__main__":
    main()
