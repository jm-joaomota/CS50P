#Ask user for an input
math = input("Math: ").strip()

#Splits the input string into three parts based on the space character
x, y, z = math.split(" ")

#Converts x and y in float numbers
num1 = float(x)
num2 = float(z)

#Do the maths.
#.1f control the precision of the output

if y == "+":
    result = num1+num2
    print(f"{result:.1f}")
elif y == "-":
    result = num1-num2
    print(f"{result:.1f}")
elif y == "*":
    result = num1*num2
    print(f"{result:.1f}")
elif y == "/":
    result = num1/num2
    print(f"{result:.1f}")

