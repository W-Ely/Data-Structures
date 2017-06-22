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

    def __init__(self, iterable=None):
        """Init with or without iterable but only nums."""
        self._root = None
        self._length = 0
        self._depth = {'r': 0, 'l': 0}
        if not iterable:
            pass
        elif iterable and self.check_value(iterable):
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
            if not self._root:
                self._root = Node(val)
                self._length += 1
                self._depth = {'r': 1, 'l': 1}
            else:
                count_depth = 1
                current_node = self._root
                if val > current_node.val:
                    side = 'r'
                if val < current_node.val:
                    side = 'l'
                while current_node:
                    count_depth += 1
                    if val > current_node.val:
                        if current_node.right:
                            current_node = current_node.right
                            continue
                        else:
                            current_node.right = Node(val)
                            self._length += 1
                            self._depth[side] = count_depth
                    elif val < current_node.val:
                        if current_node.left:
                            current_node = current_node.left
                            continue
                        else:
                            current_node.left = Node(val)
                            self._length += 1
                            self._depth[side] = count_depth
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
        return self._length

    def depth(self):
        """Return an integer representing the total number of levels in tree.

        If there are no values, depth is 0, if one value the depth should be 1,
        if two values it will be 2, if three values it may be 2 or 3.
        """
        return max([depth for side, depth in self._depth.items()])

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        if self.search(val):
            return True
        return False

    def balance(self):
        """Return an integer, positive, negative or zero.

        that represents how well balanced the tree is.
        Trees which are higher on the left than the right should return a
        positive value, trees which are higher on the right than the left
        should return a negative value. An ideally-balanced tree should
        return 0.
        """
        return self._depth['l'] - self._depth['r']

    def in_order(self, node=None, start=True):
        """Return a generator that will return the values in the tree.

        using in-order traversal, one at a time.
        """
        if start:
            node = self._root
        if node:
            for val in self.in_order(node.left, False):
                yield val
            yield node.val
            for val in self.in_order(node.right, False):
                yield val

    def pre_order(self, node=None, start=True):
        """Return a generator that will return the values in the tree.

        using pre-order traversal, one at a time.
        """
        if start:
            node = self._root
        if node:
            yield node.val
            for val in self.pre_order(node.left, False):
                yield val
            for val in self.pre_order(node.right, False):
                yield val

    def post_order(self, node=None, start=True):
        """Return a generator that will return the values in the tree.

        using post_order traversal, one at a time.
        """
        if start:
            node = self._root
        if node:
            for val in self.post_order(node.left, False):
                yield val
            for val in self.post_order(node.right, False):
                yield val
            yield node.val

    def breadth_first(self):
        """Return a generator that will return the values in the tree.

        using breadth-first traversal, one at a time.
        """
        if self._root:
            nodes = [self._root]
            for node in nodes:
                try:
                    nodes.append(node.left)
                except(AttributeError):
                    pass
                try:
                    nodes.append(node.right)
                except(AttributeError):
                    pass
                try:
                    yield node.val
                except(AttributeError):
                    pass

    def delete(self, val):
        """Remove value from the tree if present.

        Return None if not present.
        """
        # current_node = self._root
        # prev_node = None
        # direction = None
        # while current_node:
        #     if val > current_node.val:
        #         if current_node.right:
        #             prev_node, current_node = current_node, current_node.right
        #             direction = 'right'
        #             continue
        #         return
        #     elif val < current_node.val:
        #         if current_node.left:
        #             prev_node, current_node = current_node, current_node.left
        #             direction = 'left'
        #             continue
        #         return
        #     else:
        #         delete current_node
        # return
        pass

    def __len__(self):
        """Return the length."""
        return self.size()


def test(search_val):  # pragma: no cover
    """Test searchs."""
    tree = Bst([num for num in range(100)][::-1])
    tree.search(search_val)


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer('test(100)', "from __main__ import test")
    worst = Timer('test(1)', "from __main__ import test")
    print("#================= best case search 1000x ==============#")
    print(best.timeit(number=1000))
    print('')
    print("#================= worse case search 1000x==============#")
    print(worst.timeit(number=1000))
    print('')
