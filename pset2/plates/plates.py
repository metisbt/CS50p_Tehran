def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.strip()
    v = ""
    num = 0
    sym = [" ", "!", "@", ".", ",", ":", ";", '"', "'", "?","(", ")", "[", "]", "-", "_", "/", "//", "\\", "`", "#", "*"]

    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for c in s:
                if c not in sym:
                    if c.isnumeric() and num == 0 and c != "0":
                        num += 1
                        v += c
                    elif c.isnumeric() and num > 0:
                        num += 1
                        v += c
                    elif c.isalpha() and num == 0:
                        v += c

    if v == s:
        return True
    else:
        return False




main()