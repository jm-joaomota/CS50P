#Ask user for a greeting

greet = str(input("Geeting: ")).lower().strip()

if greet.startswith("hello"):
    print("0")
elif greet.startswith("h"):
    print("20")
else:
    print("100")

