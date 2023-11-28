from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    d = input("Date of Birth: ").strip()
    print(d_to_t(cal_date(check_date(d))))




def check_date(d):
    try:
        return date.fromisoformat(d)
    except ValueError:
        sys.exit("Invalid date")

def cal_date(m):
    now = date.today()
    dif = now - m
    return dif.days * 24 * 60

def d_to_t(dig):
    dig = p.number_to_words(dig, andword="")
    return dig.capitalize() + " minutes"

if __name__ == "__main__":
    main()