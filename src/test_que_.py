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
    assert queue_one_item.length == 0
    assert queue_one_item._que.head is None
    assert queue_one_item._que.tail is None


def test_shif_5_values(queue_five_items):
    """Test dequeue with 5 values in the queue and check it equals value."""
    assert queue_five_items.dequeue() == "apple"
    assert queue_five_items._que.head.value == "potato"
    assert queue_five_items._que.tail.value == "car"


def test_dequeue_with_empty_list(queue):
    """Dequeue raises error on empy list."""
    with pytest.raises(IndexError):
        queue.dequeue()


def test_len_empty_list(queue):
    """Get the length of the queue."""
    assert len(queue) == 0


def test_len_one_value(queue_one_item):
    """Test the length with one value in the queue."""
    assert len(queue_one_item) == 1


def test_len_five_values(queue_five_items):
    """Test the length with five values in the queue."""
    assert len(queue_five_items) == 5
