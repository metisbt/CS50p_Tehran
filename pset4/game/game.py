import random

while True:
    try:
        l = int(input("Level: ").strip())

        if l >= 1:
            r = random.randint(1, l)

            while True:
                try:
                    number = int(input("Guess: ").strip())

                    if number > r:
                        print("Too large!")
                    elif number < r:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
                except (TypeError, ValueError):
                    continue

            break
    except (TypeError, ValueError):
        continue