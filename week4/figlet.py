import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# list of fonts
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Ivalid Usage")

text = str(input("Input: "))
print(figlet.renderText(text))
