"""Testing module for priority queue."""
import pytest


@pytest.fixture
def empty_priority_queue():
    """Return empty initialized Priority Queue."""
    from priority_queue import PriorityQueue
    return PriorityQueue()


def test_priority_queue_init(empty_priority_queue):
    """Test priority queue init."""
    assert empty_priority_queue is not None


def test_priority_queue_iter_not_none():
    """Test insert into priority queue when iter is not None."""
    from priority_queue import PriorityQueue
    new_priority_queue = PriorityQueue([('potato', 3)])
    new_priority_queue.insert('strawberry', 2)
    assert new_priority_queue.pop() == 'strawberry'


def test_priority_queue_insert(empty_priority_queue):
    """Test insert into empty priority queue."""
    empty_priority_queue.insert('val', 1)
    assert empty_priority_queue.pop() == 'val'


def test_priority_queue_insert_default_priority(empty_priority_queue):
    """Assert peek without changing authority."""
    empty_priority_queue.insert('mango')
    assert empty_priority_queue.peek() == 'mango'


def test_pop_empty(empty_priority_queue):
    """Test pop on empty priority queue raises IndexError."""
    with pytest.raises(IndexError, message="Cannot pop from an empty priority queue."):
        empty_priority_queue.pop()


def test_pop_non_empty(empty_priority_queue):
    """Test pop returns correct item."""
    empty_priority_queue.insert('strawberry', 2)
    empty_priority_queue.insert('pancake', 1)
    assert empty_priority_queue.pop() == 'pancake'
    assert empty_priority_queue.pop() == 'strawberry'


def test_pop_insert_priority_queue():
    """Test insert to priority queue."""
    from priority_queue import PriorityQueue
    priority_queue = PriorityQueue()
    priority_queue.insert('strawberry', 2)
    priority_queue.insert('pancake', 2)
    assert priority_queue.pop() == "strawberry"
    assert priority_queue.pop() == "pancake"
