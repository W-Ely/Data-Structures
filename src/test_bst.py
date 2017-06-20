"""Tests for bst module."""

import pytest


@pytest.fixture
def bst_empty():
    """Create a binary search tree."""
    from bst import Bst
    return Bst()


@pytest.fixture
def bst_left_balance():
    r"""Create a binary search tree 5 numbers snake.

                    5
                   /
                  4
                 /
                1
                 \
                  3
                 /
                2
    depth: 5
    balance: 1
    """
    from bst import Bst
    return Bst([5, 4, 1, 3, 2])


@pytest.fixture
def bst_balanced():
    r"""Create a binary search tree 5 numbers.

                     5
                   /   \
                  2     6
                 / \     \
                1   3     7
    depth: 3
    balance: 0
    """
    from bst import Bst
    return Bst([5, 6, 2, 3, 1, 7])


@pytest.fixture
def bst_right_balance():
    r"""Create a binary search tree 5 numbers.

                     5
                   /   \
                  2     8
                       / \
                      6   9
                       \
                        7
    depth: 4
    balance: -1
    """
    from bst import Bst
    return Bst([5, 8, 6, 9, 2, 7])


@pytest.fixture
def bst_100_rand():
    """100 random numbers in bst."""
    from bst import Bst
    from random import shuffle
    rando = [num for num in range(100)]
    shuffle(rando)
    tree = Bst(rando)
    return tree


def test_initalizing_with_non_iterable_or_not_numbers_raises_ValueError():
    """Init returns Value error with with non-numbers or non-iterables."""
    from bst import Bst
    with pytest.raises(TypeError):
        Bst("dfsdfadgasdg")


def test_insert_must_be_a_number(bst_empty):
    """Raise TypeError on non number insert."""
    with pytest.raises(TypeError):
        bst_empty.insert("dfsdfadgasdg")


def test_insert_to_empty_tree_increases_tree_length(bst_empty):
    """Insert increses length."""
    bst_empty.insert(1)
    assert len(bst_empty) == 1


def test_insert_adds_value_to_tree(bst_balanced):
    """Value added to tree."""
    bst_balanced.insert(15)
    assert bst_balanced.contains(15) is True
    assert bst_balanced.search(15).val == 15


def test_insert_will_not_duplicate_value(bst_balanced):
    """Value not added twice."""
    bst_balanced.insert(6)
    assert bst_balanced.size() == 6


def test_insert_to_balanced_tree_changes_balance(bst_balanced):
    """Balance changes."""
    assert bst_balanced.balance() == 0
    bst_balanced.insert(4)
    assert bst_balanced.balance() == 1


def test_search_finds_node(bst_balanced):
    """Search returns node with value."""
    assert bst_balanced.search(1).val == 1


def test_search_returns_none_when_value_not_in_tree(bst_balanced):
    """Search returns None."""
    assert bst_balanced.search(25) is None


def test_size_is_correct_on_empty_tree(bst_empty):
    """Tree size is accurate."""
    assert bst_empty.size() == 0


def test_size_is_correct_on_filled_tree(bst_100_rand):
    """Tree size is accurate."""
    assert bst_100_rand.size() == 100


def test_depth_returns_zero_on_empty_tree(bst_empty):
    """Return 0 on empty tree."""
    assert bst_empty.depth() == 0


def test_depth_returns_correct_value_balanced_tree(bst_balanced):
    """Return value on tree."""
    assert bst_balanced.depth() == 3


def test_depth_returns_correct_value_right_balanced_tree(bst_right_balance):
    """Return value on empty tree."""
    assert bst_right_balance.depth() == 4


def test_depth_returns_correct_value_left_balanced_tree(bst_left_balance):
    """Return value on empty tree."""
    assert bst_left_balance.depth() == 5


def test_contains_returns_false_on_empty_tree(bst_empty):
    """False on empty tree."""
    assert bst_empty.contains(4) is False


def test_contains_returns_false_on_balanced_tree(bst_balanced):
    """False on balanced tree."""
    assert bst_balanced.contains(25) is False


def test_contains_returns_false_on_right_balanced_tree(bst_right_balance):
    """False on right balanced tree."""
    assert bst_right_balance.contains(25) is False


def test_contains_returns_false_on_left_balanced_tree(bst_left_balance):
    """False on left balanced tree."""
    assert bst_left_balance.contains(25) is False


def test_contains_returns_true_on_tree_with_value_left(bst_left_balance):
    """Tree has value true."""
    assert bst_left_balance.contains(3) is True
    assert bst_left_balance.contains(1) is True
    assert bst_left_balance.contains(2) is True


def test_contains_returns_true_on_tree_with_value_right(bst_right_balance):
    """Tree has value true."""
    assert bst_right_balance.contains(6) is True
    assert bst_right_balance.contains(2) is True


def test_contains_returns_true_on_tree_with_value(bst_balanced):
    """Tree has value true."""
    assert bst_balanced.contains(6) is True
    assert bst_balanced.contains(3) is True


def test_balance_right_tree(bst_right_balance):
    """Tree balanced right returns -1."""
    assert bst_right_balance.balance() == -1


def test_balance_left_tree(bst_left_balance):
    """Tree balanced right returns 1."""
    assert bst_left_balance.balance() == 1


def test_balance_balanced_tree(bst_balanced):
    """Tree balanced right returns -1."""
    assert bst_balanced.balance() == 0


def test_balance_empty_tree(bst_empty):
    """Tree balanced right returns 0."""
    assert bst_empty.balance() == 0
