user_input = input("Input: ")

vowels = "AEIOUaeiou"

for vowel in vowels:
    if vowel in vowels:
        user_input = user_input.replace(vowel, "")
print(f"Output: {user_input}")

