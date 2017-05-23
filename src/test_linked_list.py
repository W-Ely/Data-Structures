"""Module test linked list."""
from linked_list import LinkedList
import pytest


def test_push():
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    assert test_linked_list.head.value == 5


def test_pop_0_0():
    """pop resets head's value to previous value"""
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(10)
    assert test_linked_list.pop() == 10
    assert test_linked_list.head.value == 5


def test_pop_0_1():
    """pop raises error on empy list"""
    test_linked_list = LinkedList()
    assert test_linked_list.pop() == "Can not pop from empty list."


def test_size():
    test_linked_list = LinkedList()
    assert test_linked_list.size() == 0
    test_linked_list.push(5)
    assert test_linked_list.size() == 1
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.pop()
    assert test_linked_list.size() == 2


def test_search():
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(5)
    test_linked_list.push(3)
    test_linked_list.push(5)
    test_linked_list.push(25)
    test_linked_list.push(5)
    assert test_linked_list.search(25).value == 25
    assert test_linked_list.search("wont find this") is None


def test_remove():
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
    with pytest.raises(AttributeError):
        test_linked_list.remove("node")


def test_display():
    pass
