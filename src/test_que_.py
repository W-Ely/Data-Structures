"""Testing module for queue assignment."""
import pytest


@pytest.fixture
def queue():
    """Create a queue."""
    from que_ import Queue
    queue = Queue()
    return queue


@pytest.fixture
def queue_one_item(queue):
    """Create a queue with one item."""
    queue.enqueue(5)
    return queue


@pytest.fixture
def queue_five_items(queue):
    """Create a queue with 5 items, first is , last is apple."""
    queue.enqueue('potato')
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue('car')
    queue.enqueue('apple')
    return queue


def test_queue_init(queue):
    """Initialize with nothing in head."""
    assert queue._que.head is None


def test_init_typeerror():
    """Can't initialize with parameter."""
    from que_ import Queue
    with pytest.raises(TypeError):
        Queue(5)


def test_enqueue(queue):
    """Enqueue adds one item to queue."""
    queue.enqueue(5)
    assert queue._que.head.value == 5


def test_enqueue_two_items(queue_one_item):
    """Enqueue 5 and 10 into queue."""
    queue_one_item.enqueue(10)
    assert queue_one_item._que.head.next_node.value == 5


def test_enqueue_three_items(queue_one_item):
    """Enqueue 3 items and check next next node's prev node and tail."""
    queue_one_item.enqueue(10)
    queue_one_item.enqueue(15)
    assert queue_one_item._que.head.next_node.next_node.prev_node.value == 10
    assert queue_one_item._que.tail.value == 5


def test_dequeue_one_value(queue_one_item):
    """Dequeue resets head's value to previous value."""
    assert queue_one_item.dequeue() == 5
    assert queue_one_item.size() == 0
    assert queue_one_item._que.head is None
    assert queue_one_item._que.tail is None


def test_shif_5_values(queue_five_items):
    """Test dequeue with 5 values in the queue and check it equals value."""
    assert queue_five_items.dequeue() == "potato"
    assert queue_five_items._que.head.value == "apple"
    assert queue_five_items._que.tail.value == 5


def test_dequeue_with_empty_list(queue):
    """Dequeue raises error on empy list."""
    with pytest.raises(IndexError):
        queue.dequeue()


def test_peek_with_empty_queue(queue):
    """Peek returns None on empty queue."""
    assert queue.peek() is None


def test_peek_with_five_in_queue(queue_five_items):
    """Peek returns end on queue of five."""
    assert queue_five_items.peek() == "potato"


def test_peek_with_one_in_queue(queue_one_item):
    """Peek returnsfirst on queue of one item."""
    assert queue_one_item.peek() == 5


def test_size_empty_list(queue):
    """Get the length of the queue."""
    assert queue.size() == 0


def test_size_one_value(queue_one_item):
    """Test the length with one value in the queue."""
    assert queue_one_item.size() == 1


def test_size_five_values(queue_five_items):
    """Test the length with five values in the queue."""
    assert queue_five_items.size() == 5
