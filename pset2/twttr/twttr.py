letters = ["i", "e", "o", "u", "a"]

text = input("Write text: ").strip()

output = ""

for letter in text:
    if letter.lower() not in letters:
        output += letter
    else:
        continue

print(output)
