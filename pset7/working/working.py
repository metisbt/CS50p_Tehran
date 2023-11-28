import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):

    try:
        time = str(re.findall(r'\d+(?:\:)?(?:\d+)? ?(?:AM)? to \d+(?:\:)?(?:\d+)? ?(?:PM)?', s, re.IGNORECASE))

        if x := re.search(r"(\d+):([0-5]+[0-9]+) AM to (\d+):([0-5]+[0-9]+) PM", time):
            if int(x.group(1)) > 12 or int(x.group(1)) < 1 or int(x.group(3)) > 12 or int(x.group(3)) < 1:
                raise ValueError
            elif int(x.group(1)) == 12 and int(x.group(3)) == 12:
                y = re.sub(r"(\d+):([0-5]+[0-9]+) AM to (\d+):([0-5]+[0-9]+) PM", f"00:00 to 12:00", time)
            elif int(x.group(1)) <= 9:
                y = re.sub(r"(\d+):([0-5]+[0-9]+) AM to (\d+):([0-5]+[0-9]+) PM", f"0{x.group(1)}:{x.group(2)} to {int(x.group(3)) + 12}:{x.group(4)}", time)
            else:
                y = re.sub(r"(\d+):([0-5]+[0-9]+) AM to (\d+):([0-5]+[0-9]+) PM", f"{x.group(1)}:{x.group(2)} to {int(x.group(3)) + 12}:{x.group(4)}", time)

        elif x := re.search(r"(\d+):?([0-5]+[0-9]+)? AM to (\d+):?([0-5]+[0-9]+)? PM", time):
            if int(x.group(1)) > 12 or int(x.group(1)) < 1 or int(x.group(3)) > 12 or int(x.group(3)) < 1:
                raise ValueError
            elif int(x.group(1)) == 12 and int(x.group(3)) == 12:
                y = re.sub(r"(\d+):?([0-5]+[0-9]+)? AM to (\d+):?([0-5]+[0-9]+)? PM", "00:00 to 12:00", time)
            elif int(x.group(1)) <= 9:
                y = re.sub(r"(\d+):?([0-5]+[0-9]+)? AM to (\d+):?([0-5]+[0-9]+)? PM", f"0{x.group(1)}:00 to {int(x.group(3)) + 12}:00", time)
            else:
                y = re.sub(r"(\d+):?([0-5]+[0-9]+)? AM to (\d+):?([0-5]+[0-9]+)? PM", f"0{x.group(1)}:00 to {int(x.group(3)) + 12}:00", time)
        else:
            raise ValueError

    except ValueError:
        raise ValueError

    else:
        return y.strip("['']")

if __name__ == "__main__":
    main()