text = input("Greeting: ").strip().lower()

if text.startswith("hello"):
    print("$0")
elif text[0] == "h":
    print("$20")
else:
    print("$100")