letters = ["i", "e", "o", "u", "a"]

def main():
    text = str(input("Write text: ").strip())
    print(f"Output: {shorten(text)}")

def shorten(word):
    output = ""

    for letter in word:
        if letter.lower() not in letters:
            output += letter
        else:
            continue

    return output


if __name__ == "__main__":
    main()