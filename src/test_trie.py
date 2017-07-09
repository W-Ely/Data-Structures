"""Test module for trie data structure."""
import pytest
from trie import Trie


@pytest.fixture
def trie():
    """Create empty tree for fixture."""
    return Trie()


@pytest.fixture
def simple(trie):
    r"""Test Simple Trie.

         trie
        /    \
       a      d
       |      |
       b      e
      / \     |
     c   $    f
     |        |
     $        $

    Simple.
    """
    trie.insert('abc')
    trie.insert('ab')
    trie.insert('def')
    return trie


def test_insert_inserts_new_string(trie):
    """Test insert adds new string."""
    trie.insert('abc')
    assert trie.contains('abc') is True
    assert list(trie.keys())[0] == 'a'
    assert list(trie['a'].keys())[0] == 'b'
    assert list(trie['a']['b'].keys())[0] == 'c'
    assert '$' in trie['a']['b']['c']


def test_insert_ignors_duplicate_string(trie):
    """Test insert doesn't add duplicate string."""
    trie.insert('abc')
    with pytest.raises(IndexError):
        list(trie.keys())[1]


def test_insert_raises_TypeError_with_invalid_value(trie):
    """Test raises TypeError."""
    with pytest.raises(TypeError):
        trie.insert('abc$')
    with pytest.raises(TypeError):
        trie.insert(1)
    with pytest.raises(TypeError):
        trie.insert('')


def test_contains_True_if_value_in_trie(trie):
    """Test contains True is value present."""
    trie.insert('abc')
    assert trie.contains('abc') is True


def test_contains_False_if_value_not_in_trie(trie):
    """Test contains False is value not in trie."""
    trie.insert('abc')
    assert trie.contains('not') is False


def test_contains_False_if_value_doesnt_end_with_termination_char(trie):
    """Test contains False without terminator."""
    trie.insert('abc')
    assert trie.contains('ab') is False


def test_size_increases_with_insert(trie):
    """Test trie increase with insert."""
    assert trie.size() == 0
    trie.insert('abc')
    assert trie.size() == 1


def test_size_does_not_increase_with_attempt_to_add_duplicate(trie):
    """Test size doesn't increase with duplicate insert."""
    trie.insert('abc')
    trie.insert('ab')
    assert trie.size() == 2
    trie.insert('abc')
    assert trie.size() == 2


def test_size_decrease_on_remove(trie):
    """Test remove decreases size."""
    trie.insert('abc')
    trie.insert('def')
    assert trie.size() == 2
    trie.remove('abc')
    assert trie.size() == 1


def test_size_doesnt_decrease_if_item_not_found(trie):
    """Test size doesn't decrease if value not in trie."""
    trie.insert('abc')
    trie.insert('def')
    assert trie.size() == 2
    with pytest.raises(KeyError):
        trie.remove('not in tree')
    assert trie.size() == 2


def test_remove_removes_value_from_trie(trie):
    """Test removes value from trie."""
    trie.insert('abc')
    trie.insert('def')
    trie.remove('abc')
    assert not trie.contains('abc')
    assert trie.size() == 1
    assert 'a' not in trie.keys()


def test_remove_removes_only_terminator_when_the_rest_should_remain(simple):
    """Test removes teminator leaving other when required.

    Remove 'ab', 'abc' should remain.
    """
    assert simple.size() == 3
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    simple.remove('ab')
    assert simple.size() == 2
    assert '$' not in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']


def test_remove_branch_from_trie(simple):
    """Test remove branch."""
    assert simple.size() == 3
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    simple.remove('abc')
    assert simple.size() == 2
    assert '$' in simple['a']['b']
    assert 'c' not in simple['a']['b']
    assert '$' in simple['d']['e']['f']


def test_remove_branch_from_root_of_trie(simple):
    """Test remove branch."""
    assert simple.size() == 3
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    simple.remove('def')
    assert simple.size() == 2
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert 'd' not in simple
