def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")


def shorten(word):
    vowels = "AEIOUaeiou"
    result = word
    for vowel in vowels:
        result = result.replace(vowel, "")
    return result


if __name__ == "__main__":
    main()
