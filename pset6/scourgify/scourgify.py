import os
import sys
import csv


def main():
    if len(sys.argv) < 3:
        print("Too few command-line argument!")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line argument!")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
       scaniii(sys.argv[1], sys.argv[2])

def scaniii(infile, outfile):
    with open(infile, "r") as inputfile:
        indata = csv.DictReader(inputfile, delimiter=",")

        with open(outfile, "w") as outputfile:
            person_data = ["first_name", "last_name", "home"]
            outdata = csv.DictWriter(outputfile, fieldnames=person_data)
            outdata.writeheader()

            for i in indata:
                last, first = i["name"].split(",")
                house = i["house"]

                outdata.writerow({"first_name": first.strip(),
                                "last_name": last,
                                "home": house})

if __name__ == "__main__":
    main()