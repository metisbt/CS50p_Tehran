import os
import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line argument!")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line argument!")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Invalid input - path")
        sys.exit(1)
    elif not checkp(sys.argv[1]) and checkp(sys.argv[2]):
        print("Invalid input")
        sys.exit(1)
    elif not samep(sys.argv[1], sys.argv[2]):
        print("Input and output have different extension")
        sys.exit(1)
    else:
       shirtw(sys.argv[1], sys.argv[2])


def checkp(inputfile):
    _, p = inputfile.split(".")

    if p in ["jpg", "jpeg", "png"]:
        return True
    else:
        return False


def samep(inputfile, outputfile):
    _, p = inputfile.split(".")

    if outputfile.endswith(p):
        return True
    else:
        return False

def shirtw(input_file, output_file):
    shirt = Image.open("shirt.png")
    imageuser = Image.open(input_file)

    x, y = shirt.size
    imageuser = ImageOps.fit(imageuser, (x, y))

    imageuser.paste(shirt, shirt)
    imageuser.save(output_file)

if __name__ == "__main__":
    main()