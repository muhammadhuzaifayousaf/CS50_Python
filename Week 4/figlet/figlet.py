import sys
from pyfiglet import Figlet

if len(sys.argv) == 1:
    figlet = Figlet()
    str = input("Input: ")
    print(figlet.renderText(str))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    f = sys.argv[2]
    figlet = Figlet(font=f)
    str = input("Input: ")
    print(figlet.renderText(str))
else:
    print("Invalid usage")
    sys.exit(1)
