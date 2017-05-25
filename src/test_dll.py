"""Testing module for doubly linked list."""
import pytest


@pytest.fixture
def dll():
    """Create a doubly linked list."""
    from dll import Dll
    dll = Dll()
    return dll


def test_dll_init():
    """Can be Initalized with iterable or nothing only."""
    from dll import Dll
    dll = Dll()
    assert dll.head is None
    with pytest.raises(TypeError):
        Dll(5)


def test_push(dll):
    """Push adds to doubly linked list."""
    dll.push(5)
    assert dll.head.value == 5
    dll.push(10)
    assert dll.head.next_node.value == 5
    dll.push(15)
    assert dll.head.next_node.next_node.prev_node.value == 10
    assert dll.tail.value == 5


def test_append(dll):
    """Append value to end of doubly linked list."""
    dll.append("potato")
    assert dll.tail.value == "potato"
    assert dll.head.value == "potato"
    dll.append(10)
    assert dll.tail.prev_node.value == "potato"
    dll.append(15)
    assert dll.tail.prev_node.prev_node.next_node.value == 10
    assert dll.head.value == "potato"
    assert dll.tail.value == 15


def test_pop_0_0(dll):
    """pop resets head's value to previous value"""
    dll.push(5)
    assert dll.pop() == 5
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None
    dll.push(5)
    dll.push(10)
    dll.append(15)
    assert dll.pop() == 10
    assert dll.head.value == 5
    assert dll.tail.value == 15


def test_pop_0_1(dll):
    """pop raises error on empy list"""
    assert dll.pop() == "Can not pop from empty list."


def test_len(dll):
    """Gets the length."""
    assert dll.__len__() == 0
    dll.push(5)
    assert len(dll) == 1
    dll.push(5)
    dll.append("potato")
    assert len(dll) == 3
    dll.push(5)
    dll.pop()
    assert dll.__len__() == 3


# def test_remove():
#     """Removes a node and maintains links."""
#     test_linked_list = LinkedList()
#     test_linked_list.push(5)
#     test_linked_list.push(5)
#     test_linked_list.push(3)
#     test_linked_list.push(5)
#     test_linked_list.push("remove me")
#     test_linked_list.push(25)
#     remove_this = test_linked_list.search("remove me")
#     test_linked_list.remove(remove_this)
#     assert test_linked_list.size() == 5
#     assert test_linked_list.search(25).value == 25
#     with pytest.raises(AttributeError):
#         test_linked_list.remove("node")


def test__repr(dll):
    """displays the list as a tuple"""
    dll.push(5)
    dll.push(10)
    assert dll.__repr__() == '(10, 5)'
    dll.append(5)
    assert dll.__repr__() == '(10, 5, 5)'
