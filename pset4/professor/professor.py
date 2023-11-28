import random


def main():
    setlevel = get_level()
    pset = generate_integer(setlevel)

    score = 0

    for q in pset:
        damage = 0

        while True:
            try:
                answer = int(input(f"{q} = "))
                x, y = q.strip().split("+")

                if damage == 2:
                    print("EEE")
                    print(f"{q} = {int(x) + int(y)}")
                    break
                elif answer != (int(x) + int(y)):
                    damage += 1
                    print("EEE")
                else:
                    score += 1
                    damage = 0
                    break
            except ValueError:
                print("EEE")
                damage += 1
                continue


    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())

            if level in [1, 2, 3]:
                return level
            else:
                continue

        except ValueError:
            continue



def generate_integer(level):
    pset = []

    if level == 1:
        l = 0
        h = 9
        for _ in range(0,10):
            pset.append(f"{random.randint(l, h)} + {random.randint(l, h)}")

        return pset

    elif level == 2:
        l1 = 10
        h1 = 99
        for _ in range(0,10):
            pset.append(f"{random.randint(l1, h1)} + {random.randint(l1, h1)}")

        return pset

    else:
        l2 = 100
        h2 = 999
        for _ in range(0,10):
            pset.append(f"{random.randint(l2, h2)} + {random.randint(l2, h2)}")

        return pset



if __name__ == "__main__":
    main()