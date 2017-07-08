"""Test module for trie data structure."""
import pytest
from trie import Trie


@pytest.fixture
def trie():
    """Create empty tree for fixture."""
    return Trie()


def test_insert_inserts_new_string(trie):
    """Test insert adds new string."""
    trie.insert('abc')
    assert trie.contains('abc') is True
    assert list(trie.keys())[0] == 'a'
    assert list(trie['a'].keys())[0] == 'b'
    assert list(trie['a']['b'].keys())[0] == 'c'
    assert trie['a']['b']['c'] == '$'


def test_insert_ignors_duplicate_string(trie):
    """Test insert doesn't add duplicate string."""
    trie.insert('abc')
    with pytest.raises(IndexError):
        list(trie.keys())[1]


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
# size(self): will return the total number of words contained within the trie. 0 if empty.
# remove(self, string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception.
