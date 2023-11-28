coin = [5, 10, 25]
c = 50
g = 0

while g < c:
    print(f"Amount Due: {c - g}")
    num = int(input("Next coin: "))
    if num in coin:
        g += num
    else:
        continue
print(f"Change Owed: {g - c}")