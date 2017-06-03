"""Module tests binheap."""
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


@pytest.fixture
def binheap_100_rand():
    from binheap import Binheap
    from random import randint
    heap = Binheap([randint(1, 1000) for _ in range(15)])
    return heap


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
    binheap_empty.push(1)
    assert len(binheap_empty) == 1


def test_push_smaller_num_to_heap_changes_order_of_heap(binheap_five_rand_num):
    """."""
    binheap_five_rand_num.push(0)
    assert binheap_five_rand_num.pop() == 0


def test_heap_rand_100_placed_in_order(binheap_100_rand):
    """."""
    for index, num in enumerate(binheap_100_rand):
        if index * 2 + 1 <= len(binheap_100_rand) - 1:
            assert num < binheap_100_rand[index * 2 + 1]
        if index * 2 + 2 <= len(binheap_100_rand) - 1:
            assert num < binheap_100_rand[index * 2 + 2]


def test_heap_rand_100_removes_in_order(binheap_100_rand):
    """."""
    temp_a = binheap_100_rand.pop()
    temp_b = binheap_100_rand.pop()
    for _ in range(len(binheap_100_rand) - 1):
        assert temp_a < temp_b
        temp_a, temp_b = temp_b, binheap_100_rand.pop()
