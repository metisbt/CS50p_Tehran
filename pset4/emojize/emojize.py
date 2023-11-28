from emoji import emojize

e = input("Input: ").strip()
print(f"Output: {emojize(e, language='alias')}")