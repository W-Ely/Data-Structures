"""Module implements binary heap data structure."""


class Binheap(list):
    """Create binary heap."""

    def __init__(self,  iterable=None):
        """Initalize with or without iterable."""
        if iterable and self.checkiterable(iterable):
                for num in iterable:
                    self.push(num)
        else:
            raise ValueError('Must be iterable and all numbers.')

    def push(self, val):
        """."""
        list.append(self, val)
        self.bubbleUp(len(self))

    def bubbleUp(self, indexPlusOne):
        """."""
        print('bubbling')
        i = indexPlusOne - 1
        while i // 2 >= 0:
            print('bubbling while ')
            if self[i] < self[i // 2]:
                temp = self[i // 2]
                self[i // 2], self[i] = self[i], temp
            if i == 0:
                break
            i = i // 2

    def bubbuleDown(self):
        """."""
        pass

    def getSmallestChildsIndex(self):
        """."""
        pass

    def checkiterable(self, iterable):
        """."""
        allnumeric = True
        for item in iterable:
            if type(item) not in [int, float]:
                allnumeric = False
        return allnumeric
