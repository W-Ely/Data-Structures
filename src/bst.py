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
                return self._insert(val, self._root)
        else:
            raise TypeError('Must be a number.')

    def _insert(self, val, node):
        """Handle insert recursivly. Re-balance at each level."""
        current_node = node
        if val > current_node.val:
            if current_node.right:
                current_node = current_node.right
                self._insert(val, current_node)
            else:
                current_node.right = Node(val)
                self._length += 1
        elif val < current_node.val:
            if current_node.left:
                current_node = current_node.left
                self._insert(val, current_node)
            else:
                current_node.left = Node(val)
                self._length += 1
        else:
            return

    def search(self, val, prev=False):
        """Return the node containing that value, else None."""
        current_node = self._root
        parent = None
        direction = None
        while current_node:
            if val > current_node.val:
                if current_node.right:
                    parent, current_node = current_node, current_node.right
                    direction = 'right'
                    continue
                else:
                    return
            elif val < current_node.val:
                if current_node.left:
                    parent, current_node = current_node, current_node.left
                    direction = 'left'
                    continue
                else:
                    return
            else:
                break
        if prev:
            return current_node, parent, direction
        return current_node

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
        if (left_depth > right_depth):
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

    def delete(self, val):
        """Remove value from the tree if present.

        Return None always.
        """
        current_node, prev_node, par_to_chi_dir = self.search(val, True)
        if not current_node:
            return
        succ, prev_succ, balance, direct = self._find_succ(current_node)
        if not succ:  # Successor gets non-relative child of node to remove
            if not par_to_chi_dir:
                self._root = None
            else:
                setattr(prev_node, par_to_chi_dir, None)
        else:
            setattr(
                succ,
                direct[balance * -1],
                getattr(current_node, direct[balance * -1])
            )
            if succ is not prev_succ:  # Successor parent gets successor child
                setattr(
                    prev_succ,
                    direct[balance * -1],
                    getattr(succ, direct[balance])
                )
            # Successor child becomes the current nodes other child
            if getattr(current_node, direct[balance]) is not succ:
                setattr(
                    succ,
                    direct[balance],
                    getattr(current_node, direct[balance])
                )
            if prev_node is None:  # Parent deleted node connects to successor
                self._root = succ
            elif prev_node.val < current_node.val:
                prev_node.right = succ
            else:
                prev_node.left = succ
        self._length -= 1
        return

    def _find_succ(self, node):
        """Find the successor node of the node to delete."""
        balance = self.balance(node)
        if balance < 0:
            balance = -1
        if balance >= 0:
            balance = 1
        direct = {1: 'right', -1: 'left'}
        succ = getattr(node, direct[balance])
        prev_succ = getattr(node, direct[balance])
        if hasattr(succ, direct[balance * -1]):
            while getattr(succ, direct[balance * -1]):
                prev_succ, succ = succ, getattr(succ, direct[balance * -1])
        return succ, prev_succ, balance, direct

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
