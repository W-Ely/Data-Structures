"""A trie data structure."""


class Trie(dict):
    """Create Trie data structure."""

    def __init__(self):
        """Inialize trie."""
        self._length = 0

    def insert(self, string):
        """Insert the string into the trie.

        If char in the string is already present, it will be ignored.
        """
        if string and type(string) is str and '$' not in string:
            temp = self
            for char in string:
                try:
                    temp = temp[char]
                    if char == string[-1] and '$' not in temp:
                        temp.update({'$': None})
                        self._length += 1
                except KeyError:
                    if char == string[-1]:
                        temp[char] = {'$': None}
                        self._length += 1
                    else:
                        temp.update({char: {}})
                        temp = temp[char]
            return
        raise TypeError('Invalid String.')

    def contains(self, string):
        """Return True if the string is in the trie, False if not."""
        temp = self
        try:
            for char in string:
                temp = temp[char]
            return '$' in temp.keys()
        except KeyError:
            return False

    def size(self):
        """Return the total number of words contained within the trie.

        0 if empty.
        """
        return self._length

    def remove(self, string):
        """Remove the given string from the trie.

        If the word doesn't exist, will raise an appropriate exception.
        """
        temp = self
        try:
            for char in string:
                if len(temp[char].keys()) > 1:
                    temp = temp[char]
                else:
                    del temp[char]
                    self._length -= 1
                    return
        except KeyError:
            raise KeyError("Value on it trie.")


trie = Trie()
trie.insert('test')
print(trie)
print(trie.contains('test'))  # True
print(trie.contains('no'))  # False
print(trie.size())  # 1
trie.remove('test')
print(trie.size())  # 0
print(trie.contains('test'))  # False
print(trie)
