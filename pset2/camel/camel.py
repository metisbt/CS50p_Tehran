text = input("camelcase: ").strip()

s = ""

for l in text:
    if l.isupper():
        s += "_"
        s += l.lower()
    else:
        s += l

print(f"snake_case: {s}")