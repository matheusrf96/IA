import numpy as np


class OrderedArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def get_values(self):
        if self.last_position == -1:
            print('Empty array')
        else:
            for i in range(self.last_position + 1):
                print(f'{i} - {self.values[i]}')

        print('\n')

    # O(n)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('Max capacity reached')
            return

        position = 0

        for i in range(self.last_position + 1):
            position = i

            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position

        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1


array = OrderedArray(10)
array.get_values()

array.insert(5)
array.get_values()

array.insert(3)
array.get_values()

array.insert(7)
array.get_values()

array.insert(11)
array.get_values()
