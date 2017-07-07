"""A trie data structure."""


class Trie(dict):
    """Create Trie data structure."""

    def __init__(self):
        """Init a trie."""
        pass

    def insert(self, string):
        """Insert the input string into the trie.

        If char in the input string is already present, it will be ignored.
        """
        pass

    def contains(self, string):
        """Return True if the string is in the trie, False if not."""
        pass

    def size(self):
        """Return the total number of words contained within the trie.

        0 if empty.
        """
        pass

    def remove(self, string):
        """Remove the given string from the trie.

        If the word doesn't exist, will raise an appropriate exception.
        """
        pass
