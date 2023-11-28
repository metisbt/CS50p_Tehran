import inflect

p = inflect.engine()
n = []

while True:

    try:
        n.append(str(input("Write name: ").strip()))
    except (EOFError, KeyError):
        print(f"Adieu, adieu, to {p.join(n)}")
        quit()