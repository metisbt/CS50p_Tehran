name = {}

while True:
    try:
        n = input().strip().lower()
        if n in name:
            name[n] += 1
        else:
            name[n] = 1
    except (EOFError, KeyError):
        for i in sorted(name, key = lambda x: name[x],  reverse = True):
            print(f"{name[i]} {i.upper()}")
        quit()
