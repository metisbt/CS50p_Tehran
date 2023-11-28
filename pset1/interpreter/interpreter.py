n = input("Enter expresion: ").strip().split(" ")

if n[1] == "+":
    answer = float(n[0]) + float(n[2])
elif n[1] == "-":
    answer = float(n[0]) - float(n[2])
elif n[1] == "/":
    answer = float(n[0]) / float(n[2])
elif n[1] == "*":
    answer = float(n[0]) * float(n[2])

print(f"{answer:.1f}")