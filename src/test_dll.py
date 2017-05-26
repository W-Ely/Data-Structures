"""Testing module for doubly linked list."""
import pytest


@pytest.fixture
def dll():
    """Create a doubly linked list."""
    from dll import Dll
    dll = Dll()
    return dll


@pytest.fixture
def dll_one_item(dll):
    """Create a dll with one item."""
    dll.push(5)
    return dll


@pytest.fixture
def dll_five_items(dll):
    """Create a dll with 5 items, first is potato, last is apple."""
    dll.append('potato')
    dll.append(5)
    dll.append(10)
    dll.append('car')
    dll.append('apple')
    return dll


def test_dll_init(dll):
    """Initialize with nothing in head."""
    assert dll.head is None


def test_init_typeerror():
    """Can't initialize with parameter."""
    from dll import Dll
    with pytest.raises(TypeError):
        Dll(5)


def test_push(dll):
    """Push adds to doubly linked list."""
    dll.push(5)
    assert dll.head.value == 5


def test_push_two_items(dll_one_item):
    """Push 5 and 10 into dll."""
    dll_one_item.push(10)
    assert dll_one_item.head.next_node.value == 5


def test_push_three_items(dll_one_item):
    """Push 3 items to dll and check next next node's prev node and tail."""
    dll_one_item.push(10)
    dll_one_item.push(15)
    assert dll_one_item.head.next_node.next_node.prev_node.value == 10
    assert dll_one_item.tail.value == 5


def test_append(dll):
    """Append value to end of doubly linked list."""
    dll.append("potato")
    assert dll.tail.value == "potato"
    assert dll.head.value == "potato"


def test_append_two_item(dll_one_item):
    """Append 2 items to the dll check the head and the tail values."""
    dll_one_item.append('potato')
    assert dll_one_item.head.value == 5
    assert dll_one_item.tail.value == "potato"


def test_append_5_values(dll_five_items):
    """Append 5 values to dll and check values."""
    assert dll_five_items.tail.prev_node.value == "car"
    assert dll_five_items.tail.prev_node.prev_node.next_node.value == 'car'
    assert dll_five_items.head.value == "potato"
    assert dll_five_items.tail.value == "apple"


def test_pop_0_0(dll_one_item):
    """Pop resets head's value to previous value."""
    assert dll_one_item.pop() == 5
    assert dll_one_item.length == 0
    assert dll_one_item.head is None
    assert dll_one_item.tail is None


def test_pop_multiple_items(dll_five_items):
    """Test pop with 5 items in the dll and returns correct values."""
    assert dll_five_items.pop() == "potato"
    assert dll_five_items.head.value == 5
    assert dll_five_items.tail.value == "apple"


def test_pop_from_empty_list(dll):
    """Pop raises error on empy list."""
    with pytest.raises(IndexError):
        dll.pop()


def test_shift_one_value(dll_one_item):
    """Shift resets head's value to previous value."""
    assert dll_one_item.shift() == 5
    assert dll_one_item.length == 0
    assert dll_one_item.head is None
    assert dll_one_item.tail is None


def test_shif_5_values(dll_five_items):
    """Test shift with 5 values in the dll and check it equals value."""
    assert dll_five_items.shift() == "apple"
    assert dll_five_items.head.value == "potato"
    assert dll_five_items.tail.value == "car"


def test_shift_with_empty_list(dll):
    """Shift raises error on empy list."""
    with pytest.raises(IndexError):
        dll.shift()


def test_len_empty_list(dll):
    """Get the length."""
    assert dll.__len__() == 0


def test_len_one_value(dll_one_item):
    """Test the length with one value in the dll."""
    assert len(dll_one_item) == 1


def test_len_five_values(dll_five_items):
    """Test the length with five values in the dll."""
    assert len(dll_five_items) == 5


def test_remove_from_empty_list(dll):
    """Remove a node and maintains links."""
    with pytest.raises(IndexError):
        dll.remove(5)


def test_remove_one_item(dll_one_item):
    """Remove one node from list."""
    dll_one_item.remove(5)
    assert len(dll_one_item) == 0
    assert dll_one_item.tail is None
    assert dll_one_item.head is None


def test_remove_5_items_middle_item(dll_five_items):
    """Remove the middle item from a 5 item long dll."""
    dll_five_items.remove(10)
    assert dll_five_items.head.next_node.next_node.value == "car"
    assert dll_five_items.tail.prev_node.prev_node.value == 5


def test_remove_node_from_list(dll_five_items):
    """Remove item not in list raises AttributeError."""
    with pytest.raises(AttributeError):
        dll_five_items.remove("node")


def test__repr(dll_five_items):
    """Display the list as a tuple."""
    assert dll_five_items.__repr__() == '("potato", 5, 10, "car", "apple")'
