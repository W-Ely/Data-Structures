"""Implements Binary Search Tree data structure."""


class Node(object):
    """."""

    def __init__(self, val, left=None, right=None):
        """."""
        self.val = val
        self.left = left
        self.right = right


class Bst(object):
    """Create a binay search tree data structure."""

    def __init__(self,  iterable=None):
        """Init with or without iterable but only nums."""
        if not iterable:
            pass
        elif iterable and self.check_value(iterable):
            self._root = None
            self._length = 0
            self._depth = 0
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
            check_depth = 0
            if not self._root:
                self._root = Node(val)
            else:
                current_node = self._root
                while current_node:
                    if val > current_node.val:
                        if current_node.right:
                            current_node = current_node.right
                            continue
                        else:
                            current_node.right = Node(val)
                            self._length += 1
                    elif val < current_node.val:
                        if current_node.left:
                            current_node = current_node.left
                            continue
                        else:
                            current_node.left = Node(val)
                            self._length += 1
                    else:
                        return
        else:
            raise TypeError('Must be a number.')

    def search(self, val):
        """Return the node containing that value, else None."""
        current_node = self._root
        while current_node:
            if val > current_node.val:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    return
            elif val < current_node.val:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    return
            else:
                return current_node
        return

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
