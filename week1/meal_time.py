def main():
    time = input("What time is it: ").strip()
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("launch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours


if __name__ == "__main__":
    main()

