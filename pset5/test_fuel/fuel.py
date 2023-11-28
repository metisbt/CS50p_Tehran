def main():
    while True:
        try:
            m = input("Fraction: ").strip()
            print(gauge(convert(m)))
            break
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            continue


def convert(fraction):
    if "/" in fraction:
        a, b = fraction.split("/")
    else:
        raise UnboundLocalError("Not valid fraction")

    if a.isdigit() and b.isdigit():
        if int(a) <= int(b) and int(b) != 0:
            percentage = (int(a) / int(b)) * 100
            return percentage
        else:
            raise ZeroDivisionError("a is larger than b")
    else:
        raise ValueError("Not an integer")


def gauge(percentage):

    if int(percentage) >= 99:
        return "F"
    elif int(percentage) < 99 and int(percentage) > 1:
        return f"{percentage:.0f}%"
    else:
        return "E"


if __name__ == "__main__":
    main()
