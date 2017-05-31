"""Testing module for dequeue."""
import pytest


@pytest.fixture
def dqu():
    """Create a doubly linked list."""
    from deque import Deque
    return Deque()


@pytest.fixture
def dqu_one_item(dqu):
    """Create a dequeue with one item."""
    dqu.append(5)
    return dqu


@pytest.fixture
def dqu_five_items(dqu):
    """Create a dequeue with 5 items, first is potato, last is apple."""
    dqu.append('potato')
    dqu.append(5)
    dqu.append(10)
    dqu.append('car')
    dqu.append('apple')
    return dqu


def test_dqu_init(dqu):
    """Initialize with nothing in head."""
    assert dqu._que.head is None


def test_init_typeerror():
    """Can't initialize with parameter."""
    from dll import Dll
    with pytest.raises(TypeError):
        Dll(5)


def test_append(dqu):
    """Push adds to doubly linked list."""
    dqu.append(5)
    assert dqu._que.head.value == 5


def test_append_two_items(dqu_one_item):
    """Push 5 and 10 into dqu."""
    dqu_one_item.append(10)
    assert dqu_one_item._que.head.next_node.value == 5


def test_append_three_items(dqu_one_item):
    """Push 3 items to dqu and check next next node's prev node and tail."""
    dqu_one_item.append(10)
    dqu_one_item.append(15)
    assert dqu_one_item._que.head.next_node.next_node.prev_node.value == 10
    assert dqu_one_item._que.tail.value == 5


def test_appendleft(dqu):
    """Append value to end of doubly linked list."""
    dqu.appendleft("potato")
    assert dqu._que.tail.value == "potato"
    assert dqu._que.head.value == "potato"


def test_appendleft_two_item(dqu_one_item):
    """Append 2 items to the dqu check the head and the tail values."""
    dqu_one_item.appendleft('potato')
    assert dqu_one_item._que.head.value == 5
    assert dqu_one_item._que.tail.value == "potato"


def test_appendleft_5_values(dqu_five_items):
    """Append 5 values to dqu and check values."""
    assert dqu_five_items._que.tail.prev_node.value == 5
    assert dqu_five_items._que.tail.prev_node.prev_node.next_node.value == 5
    assert dqu_five_items._que.head.value == "apple"
    assert dqu_five_items._que.tail.value == "potato"


def test_pop_0_0(dqu_one_item):
    """Pop resets head's value to previous value."""
    assert dqu_one_item.pop() == 5
    assert dqu_one_item.size() == 0
    assert dqu_one_item._que.head is None
    assert dqu_one_item._que.tail is None


def test_pop_multiple_items(dqu_five_items):
    """Test pop with 5 items in the dqu and returns correct values."""
    assert dqu_five_items.pop() == "apple"
    assert dqu_five_items._que.head.value == "car"
    assert dqu_five_items._que.tail.value == "potato"


def test_pop_from_empty_list(dqu):
    """Pop raises error on empy list."""
    with pytest.raises(IndexError):
        dqu.pop()


def test_popleft_one_value(dqu_one_item):
    """Shift resets head's value to previous value."""
    assert dqu_one_item.popleft() == 5
    assert dqu_one_item.size() == 0
    assert dqu_one_item._que.head is None
    assert dqu_one_item._que.tail is None


def test_popleft_5_values(dqu_five_items):
    """Test popleft with 5 values in the dqu and check it equals value."""
    assert dqu_five_items.popleft() == "potato"
    assert dqu_five_items._que.head.value == "apple"
    assert dqu_five_items._que.tail.value == 5


def test_popleft_with_empty_list(dqu):
    """Popleft raises error on empy list."""
    with pytest.raises(IndexError):
        dqu.popleft()


def test_peek_with_empty_queue(dqu):
    """Peek returns None on empty dequeue."""
    assert dqu.peek() is None


def test_peek_with_five_in_queue(dqu_five_items):
    """Peek returns end on queue of five."""
    assert dqu_five_items.peek() == "apple"


def test_peek_with_one_in_queue(dqu_one_item):
    """Peek returnsfirst on dequeue of one item."""
    assert dqu_one_item.peek() == 5


def test_peekleft_with_empty_queue(dqu):
    """Peek returns None on empty dequeue."""
    assert dqu.peekleft() is None


def test_peekleft_with_five_in_queue(dqu_five_items):
    """Peek returns end on queue of five."""
    assert dqu_five_items.peekleft() == "potato"


def test_peekleft_with_one_in_queue(dqu_one_item):
    """Peek returnsfirst on queue of one item."""
    assert dqu_one_item.peekleft() == 5


def test_size_empty_list(dqu):
    """Get the size."""
    assert dqu.size() == 0


def test_size_one_value(dqu_one_item):
    """Test the size() with one value in the dqu."""
    assert dqu_one_item.size() == 1


def test_size_five_values(dqu_five_items):
    """Test the size() with five values in the dqu."""
    assert dqu_five_items.size() == 5
