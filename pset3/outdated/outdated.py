months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        inputt = input("Date: ").strip()
        if " " in inputt:
            if "," in inputt:
                month, day, year = inputt.split(" ")

                if month.title() in months:
                    day = int(day.strip(","))
                    month = int(months.index(month)) + 1

                    if month <= 12 and day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break
        else:
            month, day, year = inputt.split("/")
            if int(month) <= 12 and int(day) <= 31:
                print(f"{int(year)}-{int(month):02}-{int(day):02}")
                break
            else:
                continue

    except ValueError:
        continue

    except (EOFError, KeyError):
        print()
        quit()

    else:
        pass
