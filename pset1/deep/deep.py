text = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if text == "forty two" or text == "forty-two" or text == "42":
    print("Yes")
else:
    print("No")