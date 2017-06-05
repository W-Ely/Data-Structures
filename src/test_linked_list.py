"""Module test linked list."""
from linked_list import LinkedList
import pytest


def test_linked_list_init():
    """Can be Initalized with iterable or nothing only."""
    test_linked_list = LinkedList([1, 2, 3])
    assert test_linked_list.head.value == 3
    assert test_linked_list.head.next_node.value == 2
    assert test_linked_list.head.next_node.next_node.value == 1


def test_linked_list_raises_error():
    """Raise TypeError when initalized with number."""
    with pytest.raises(TypeError):
        LinkedList(5)


def test_push():
    """Push adds to linked list."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    assert test_linked_list.head.value == 5


def test_pop_resets_head_to_preveous_value():
    """Pop resets head's value to previous value."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(10)
    assert test_linked_list.pop() == 10
    assert test_linked_list.head.value == 5


def test_pop_0_1():
    """Pop raises error on empy list."""
    test_linked_list = LinkedList()
    with pytest.raises(ValueError):
        test_linked_list.pop()


def test_size_is_correct_through_multiple_pushes():
    """Test the size."""
    test_linked_list = LinkedList()
    assert test_linked_list.size() == 0
    test_linked_list.push(5)
    assert test_linked_list.size() == 1
    test_linked_list.push(5)
    assert test_linked_list.size() == 2


def test_size_is_correct_through_multiple_pops():
    """Test the size."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list = LinkedList()
    assert test_linked_list.size() == 3
    test_linked_list.pop()
    assert test_linked_list.size() == 2
    test_linked_list.pop()
    assert test_linked_list.size() == 1


def test_search_finds_valid_value_and_returns_node():
    """Finds a value and returns the node."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(3)
    test_linked_list.push(5)
    test_linked_list.push(25)
    test_linked_list.push(5)
    assert test_linked_list.search(25).value == 25


def test_search_returns_None_when_value_not_found():
    """Return None on value not found."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(3)
    test_linked_list.push(5)
    test_linked_list.push(25)
    test_linked_list.push(5)
    assert test_linked_list.search("wont find this") is None


def test_remove_maintains_linked_list():
    """Removes a node and maintains links."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(3)
    test_linked_list.push(5)
    test_linked_list.push("remove me")
    test_linked_list.push(25)
    remove_this = test_linked_list.search("remove me")
    test_linked_list.remove(remove_this)
    assert test_linked_list.size() == 5
    assert test_linked_list.search(25).value == 25


def test_remove_maintains_linked_list_actually_removes_item():
    """Removes a node and maintains links."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(3)
    test_linked_list.push(5)
    test_linked_list.push("remove me")
    test_linked_list.push(25)
    remove_this = test_linked_list.search("remove me")
    test_linked_list.remove(remove_this)
    assert test_linked_list.search("remove me") is None
    with pytest.raises(AttributeError):
        test_linked_list.remove("node")


def test_remove_raises_AttributeError_when_node_not_found():
    """Removes a node and maintains links."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(3)
    with pytest.raises(AttributeError):
        test_linked_list.remove("node")


def test_remove_node_from_list():
    """Remove item not in list raises AttributeError."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(3)
    test_linked_list.push(5)
    with pytest.raises(AttributeError):
        test_linked_list.remove("node")


def test_display():
    """Displays the list as a tuple."""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    assert test_linked_list.display() == '(5, 5)'
