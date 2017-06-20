"""Implements Binary Search Tree data structure."""


class Bst(object):
    """Create a binay search tree data structure."""

    def __init__(self,  iterable=None):
        """Init with or without iterable but only nums."""
        if not iterable:
            pass
        elif iterable and self.check_value(iterable):
            self.root = None
            self.length = 0
            self.depth = 0
            for num in iterable:
                self.insert(num)
        else:
            raise TypeError('Must be iterable and all numbers.')

    def check_value(self, iterable):
        """Check iterable for all numeric values."""
        allnumeric = True
        for item in iterable:
            if type(item) not in [int, float]:
                allnumeric = False
        return allnumeric

    def insert(self, val):
        """Insert the value val into the BST.

        If val is already present, it will be ignored.
        """
        if self.check_value([val]):
            self.length += 1
            if not self.root:
                self.root.value = val
            has_next = True
            while True:
                break
        else:
            raise TypeError('Must be a number.')

    def search(self, val):
        """Return the node containing that value, else None."""
        pass

    def size(self):
        """Rreturn the integer size of the BST.

        (equal to the total number of values stored in the tree).
        It will return 0 if the tree is empty.
        """
        pass

    def depth(self):
        """Return an integer representing the total number of levels in tree.

        If there are no values, depth is 0, if one value the depth should be 1,
        if two values it will be 2, if three values it may be 2 or 3.
        """
        pass

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        pass

    def balance(self):
        """Return an integer, positive, negative or zero.

        that represents how well balanced the tree is.
        Trees which are higher on the left than the right should return a
        positive value, trees which are higher on the right than the left
        should return a negative value. An ideally-balanced tree should
        return 0.
        """
        pass

    def __len__(self):
        """Return the length."""
        return self.size()


if __name__ == '__main__':
    # import timeit
    # print(timeit.timeit("test()", setup="from __main__ import test"))
    pass
