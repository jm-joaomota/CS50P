def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")


def shorten(word):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()
