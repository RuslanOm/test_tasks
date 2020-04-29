from collections import deque


class RingBufferDeq:
    def __init__(self, size_max):
        self.max = size_max
        self.data = deque()

    def append(self, x):
        if len(self.data) >= self.max:
            self.data.popleft()
            self.data.append(x)
        else:
            self.data.append(x)

    def pop(self):
        if len(self.data):
            return self.data.popleft()
        raise IndexError("pop from an empty buffer")


class RingBufferArray:

    def __init__(self, size_max):
        self.max = size_max
        self._true_size = 0
        self.head = 0
        self.tail = 0
        self.data = [None for _ in range(size_max)]

    def append(self, x):
        self.data[self.tail % self.max] = x
        self.tail += 1
        if self.tail % self.max == self.head % self.max:
            self.head += 1
        if self._true_size < self.max:
            self._true_size += 1
        self.head %= self.max
        self.tail %= self.max

    def pop(self):
        if self._true_size:
            val = self.data[self.head % self.max - 1]
            self.data[self.head % self.max - 1] = None
            self.head += 1
            self._true_size -= 1
            if self._true_size == 0:
                self.head = 0
                self.tail = 0
            self.head %= self.max
            self.tail %= self.max
            return val
        else:
            raise IndexError("pop from an empty buffer")

    def __len__(self):
        return self._true_size


if __name__ == "__main__":
    # some test code
    rba = RingBufferArray(10)
    rbq = RingBufferDeq(10)
    for i in range(15):
        rba.append(i)
        rbq.append(i)

    for i in range(10):
        print "Array buffer element", rba.pop(), "Deque buffer element", rbq.pop()
