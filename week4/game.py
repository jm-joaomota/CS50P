import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            number = random.randint(1,level)
            break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")
        else:
            print("Just Right")
            break
    except:
        pass
