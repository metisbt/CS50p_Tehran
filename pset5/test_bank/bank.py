def main():
    text = input("Greeting: ").strip().lower()
    print(f"{value(text)}")



def value(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()