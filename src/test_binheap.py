"""Module tests binheap."""

# formula i * 2 + 1 = left child, i * 2 + 2 = right child
# i is the index in the list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 0 left --> 1    0 right --> 2
# 2 left --> 5    2 right --> 6
#
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
# 2.left is 4   and 2.right is 6
# 8.left is 16  and 8.right is 18
#
import pytest


@pytest.fixture
def binheap_empty():
    """Create a binary heap."""
    from binheap import Binheap
    return Binheap()


@pytest.fixture
def binheap_five_seq_num():
    """Create a binary heap with 5 sequential numbers."""
    from binheap import Binheap
    return Binheap([0, 1, 2, 3, 4])


@pytest.fixture
def binheap_five_rand_num():
    """Create a binary heap 5 random numbers."""
    from binheap import Binheap
    return Binheap([5, 4, 1, 3, 2])


def test_pop_removes_smallest_num(binheap_five_rand_num):
    """Return lowest."""
    assert binheap_five_rand_num.pop() == 1
    assert binheap_five_rand_num.pop() == 2
    assert binheap_five_rand_num.pop() == 3
    assert binheap_five_rand_num.pop() == 4
    assert binheap_five_rand_num.pop() == 5


def test_pop_empty_heap_returns_None(binheap_empty):
    """Pop returns None on empty heap."""
    assert binheap_empty.pop() is None


def test_push_to_empty_heap_increases_heap_length(binheap_empty):
    """."""
    assert len(binheap_empty.push(1)) == 1


def test_push_smaller_num_to_heap_changes_order_of_heap(binheap_five_rand_num):
    """."""
    binheap_five_rand_num.push(0)
    assert binheap_five_rand_num.pop() == 0
