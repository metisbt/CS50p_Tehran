import sys
import random
from pyfiglet import Figlet

f = Figlet()
fonts = f.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ").strip()
    f.setFont(font = random.choice(fonts))
    print(f.renderText(text))

elif len(sys.argv) == 3:
    if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in fonts:
        text = input("Input: ").strip()
        f.setFont(font = str(sys.argv[2]))
        print(f.renderText(text))
    else:
        sys.exit("Invalid useag")

else:
    sys.exit("Invalid useag")