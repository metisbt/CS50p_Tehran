import os
import sys


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
    elif not sys.argv[1].endswith(".py"):
        print("Not a python file")
        sys.exit(1)
    else:
        print(counter(sys.argv[1]))


def counter(p_file):
    s_line = 0

    with open(p_file, "r") as pythonfile:
        lines = list(enumerate(pythonfile.readlines(), start=1))

        for xline, line in lines:
            if (
                line.strip().startswith("#")
                or line.strip().startswith("\n")
                or line.isspace()
            ):
                s_line += 1

    return int(lines[-1][0]) - s_line


if __name__ == "__main__":
    main()
