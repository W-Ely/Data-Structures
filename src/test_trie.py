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


# insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.
# contains(self, string): will return True if the string is in the trie, False if not.
# size(self): will return the total number of words contained within the trie. 0 if empty.
# remove(self, string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception.
