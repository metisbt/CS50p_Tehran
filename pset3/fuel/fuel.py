while True:
    m = input("Fraction: ").strip()

    try:
        a, b = m.split("/")

        if a.isdigit() and b.isdigit():
            if int(a) <= int(b) and int(b) != 0:
                f = (int(a) / int(b)) * 100
            else:
                continue
        else:
            continue

    except (ValueError, ZeroDivisionError):
        pass

    else:
        break

if f >= 99:
    print("F")
elif f < 99 and f > 1:
    print(f"{f:.0f}%")
else:
    print("E")