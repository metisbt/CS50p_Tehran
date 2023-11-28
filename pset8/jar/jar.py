class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not n > (self.capacity - self.size):
            self.size += n

        else:
            raise ValueError("Too many cooies!")

    def withdraw(self, n):
        if not n > (self.size):
            self.size -= n
        else:
            raise ValueError("Too few cooies!")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if not int(capacity) > 0:
            raise ValueError("Not a non-negetive integer.")
        else:
            self._capacity = capacity

    @size.setter
    def size(self, size):
        if int(size) < 0:
            raise ValueError
        else:
            self._size = size


def main():
    cookies = Jar(13)
    cookies.deposit(13)
    cookies.withdraw(1)
    print(cookies.capacity)
    print(cookies.size)


if __name__ == "__main__":
    main()