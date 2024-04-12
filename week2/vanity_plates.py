def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#check if the plate starts with 2 letters
def check_start(plate):
    if plate[0:2].isalpha():
        return True
    return False

#check if the plate has between 2 and six alphanumuerics letters

def check_lenght(plate):
    if 2 <= len(plate) <= 6 and plate.isalnum():
        return True
    return False

def check_numbers(plate):
    for index, _ in enumerate(plate):
        if plate[index].isdigit():
            if plate[index] == "0" or not plate[index:].isdigit():
                return False
            break
    return True


def is_valid(s):
    if check_start(s) and check_lenght(s) and check_numbers(s):
        return True
    return False



main()

