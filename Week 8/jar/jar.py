class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong Value")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("Exceed capacity")
        if (n + self._size) > self._capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("There are fewer cookies than asked to be removed")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
