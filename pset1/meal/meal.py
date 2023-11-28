def main():
    time_sheet = [
        {"meal" : "breakfast time", "start" : 7, "end" : 8},
        {"meal" : "lunch time", "start" : 12, "end" : 13},
        {"meal" : "dinner time", "start" : 18, "end" : 19}
    ]

    user_time = input("What time is it? ")
    user_time = float(convert(user_time))

    for time in time_sheet:
        if user_time >= float(time["start"]) and user_time <= float(time["end"]):
            print(time["meal"])
        else:
            continue


def convert(time):
    h = 0.0
    if time.rfind(" a.m.") != -1:
        time.replace(' a.m.', '')
    elif time.rfind(" p.m.") != -1:
        time.replace(' p.m.', '')
        h = 12.0

    t = time.strip().split(":")
    export = float(t[0]) + (float(t[1]) / 60) + h

    return export


if __name__ == "__main__":
    main()
