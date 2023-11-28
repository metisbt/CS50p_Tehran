import os
import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line argument!")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line argument!")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File doesn't exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
       maketabel(sys.argv[1])

def maketabel(cfile):
    with open(cfile, "r") as myfile:
        t = csv.DictReader(myfile, delimiter=",")

        print(tabulate(t, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()