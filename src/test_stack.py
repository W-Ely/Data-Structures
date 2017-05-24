"""Module test linked list."""
from stack import Stack
import pytest


def test_stack_init():
    """Can be Initalized with iterable or nothing only"""
    test_stack = Stack([1, 2, 3])
    assert test_stack.head.value == 3
    assert test_stack.head.next_node.value == 2
    assert test_stack.head.next_node.next_node.value == 1
    with pytest.raises(TypeError):
        Stack(5)


def test_pop_0_0():
    """pop resets head's value to previous value"""
    test_stack = Stack()
    test_stack.push(5)
    test_stack.push(10)
    assert test_stack.pop() == 10
    assert test_stack.head.value == 5


def test_pop_0_1():
    """pop raises error on empy list"""
    test_linked_list = Stack()
    assert test_linked_list.pop() == "Can not pop from empty list."


def test_len():
    """testing length of stack"""
    test_stack = Stack()
    assert len(test_stack) == 0
    test_stack.push(5)
    assert len(test_stack) == 1
    test_stack.push(5)
    test_stack.push(5)
    test_stack.pop()
    assert len(test_stack) == 2
