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
            else:
                self._insert(val, self._root)
        else:
            raise TypeError('Must be a number.')

    def _insert(self, val, node, parent=None):
        """Handle insert recursivly. Re-balance if needed at each level."""
        child = None
        if val > node.val:
            if node.right:
                child = self._insert(val, node.right, node)
            else:
                node.right = Node(val)
                child = node.right
                self._length += 1
        elif val < node.val:
            if node.left:
                child = self._insert(val, node.left, node)
            else:
                node.left = Node(val)
                child = node.left
                self._length += 1
        balance = self.balance(node)
        child_balance = self.balance(child)
        if balance not in range(-1, 2):
            self._rotate(
                node, balance, child, child_balance, parent
            )
        return node

    def _rotate(
            self, node, balance, child, child_balance, parent
            ):
        if balance == -2 and child_balance >= 1:  # case 1 left, right
            pivot = child.right
            node.left = pivot.right
            child.right = pivot.left
            pivot.right = node
            pivot.left = child
            if node is self._root:
                self._root = pivot
            else:
                if parent.val < node.val:
                    parent.right = pivot
                else:
                    parent.left = pivot
            return pivot
        if balance == -2 and child_balance <= 0:  # case 2 right
            node.left = child.right
            child.right = node
            if node is self._root:
                self._root = child
            else:
                if parent.val < node.val:
                    parent.right = child
                else:
                    parent.left = child
            return child
        if balance == 2 and child_balance <= 0:  # case 3 right, left
            pivot = child.left  # step 1
            node.right = pivot.left
            child.left = pivot.right
            pivot.left = node
            pivot.right = child
            if node is self._root:
                self._root = pivot
            else:
                if parent.val < node.val:
                    parent.right = pivot
                else:
                    parent.left = pivot
            return pivot
        if balance == 2 and child_balance >= 0:  # case 4 left
            node.right = child.left
            child.left = node
            if node is self._root:
                self._root = child
            else:
                if parent.val < node.val:
                    parent.right = child
                else:
                    parent.left = child
            return child

    def search(self, val):
        """Return the node containing that value, else None."""
        node = self._root
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                    continue
                else:
                    return
            elif val < node.val:
                if node.left:
                    node = node.left
                    continue
                else:
                    return
            else:
                break
        return node

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
        return self._depth(self._root)

    def _depth(self, node):
        if node is None:
            return 0
        left_depth = self._depth(node.left)
        right_depth = self._depth(node.right)
        if left_depth > right_depth:
            return left_depth + 1
        return right_depth + 1

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        if self.search(val):
            return True
        return False

    def balance(self, node=None):
        """Return an integer, positive, negative or zero.

        that represents how well balanced the tree is.
        Trees which are higher on the left than the right should return a
        positive value, trees which are higher on the right than the left
        should return a negative value. An ideally-balanced tree should
        return 0.
        """
        if self._length == 0:
            return 0
        if not node:
            node = self._root
        return self._depth(node.right) - self._depth(node.left)

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

    def delete(self, val=None):
        """Remove value from the tree if present.

        Return None always.
        """
        if not self._root:
            return
        self._root = self._delete(val, self._root)

    def _delete(self, val, node, parent=None):
        """Delete recursivly. Re-balance if needed at each level."""
        if node:
            if val > node.val:
                node.right = self._delete(val, node.right, node)
            elif val < node.val:
                node.left = self._delete(val, node.left, node)
            elif val == node.val:
                if node.left and node.right:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    self.delete(successor.val)
                    node.val = successor.val
                else:
                    if not node.left and not node.right:
                        node = None
                    elif not node.left:
                        node = node.right
                    elif not node.right:
                        node = node.left
                    self._length -= 1
            balance = self.balance(node)
            if balance not in range(-1, 2):
                if balance < -1:
                    child = node.left
                    child_balance = self.balance(child)
                elif balance > 1:
                    child = node.right
                    child_balance = self.balance(child)
                node = self._rotate(
                    node, balance, child, child_balance, parent
                )
            return node

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
