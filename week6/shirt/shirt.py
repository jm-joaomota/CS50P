import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            sys.exit("Invalid output")
        elif (
            inp[1].lower() != outp[1].lower()
        ):  # inp[0] == filename inp[1] == extension
            sys.exit("Input and output have different extensions")
        else:
            image(sys.argv[1], sys.argv[2])


def image(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            fitted_input = ImageOps.fit(input, shirt.size)
            fitted_input.paste(shirt, mask=shirt)
            fitted_input.save(output)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
