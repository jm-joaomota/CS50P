#Take input from user.

def main():
    message = input("Message")

    print(convert(message))

#Create a function that converts emoticons in emojis

def convert(text):
    return(text.replace(":)", "🙂").replace(":(", '🙁' ))

main()

