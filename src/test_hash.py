"""This is our test module for hashing data structure."""
from hash_table import HashTable
from hash_table import optimus_prime_hash
import os
import pytest


def populate_dict():
    """Populate our dictionary."""
    dictionary = []
    dictfile = "/src/test/words"
    path = os.getcwd() + dictfile
    with open(path, 'r') as words:
        for line in words:
            dictionary.append(line[:-1])
    return dictionary


DICTIONARY = populate_dict()


@pytest.fixture
def hash_table():
    """Hash table dict."""
    hash_table = HashTable(58237)
    for i, word in enumerate(DICTIONARY):
        if i % 100 == 0:
            hash_table.set(word, word)
    return hash_table


@pytest.fixture
def hash_table_prime():
    """Prime hash table dict."""
    hash_table = HashTable(58237, optimus_prime_hash)
    for word in DICTIONARY:
        hash_table.set(word, word)
    return hash_table


def test_get_returns_stored_value():
    """Test get method and see if it returns stored val."""
    hash_table = HashTable(17)
    hash_table.set('testkey', 'testval')
    assert hash_table.get("testkey") == "testval"


def test_set_stores_value_given_key():
    """Test set method stores given val using given key."""
    hash_table = HashTable(17)
    hash_table.set('testkey2', 'testval2')
    assert hash_table.get("testkey2") == "testval2"


def test_enormous_amount_of_info(hash_table):
    """Time to break the code."""
    for i, word in enumerate(DICTIONARY):
        if i % 100 == 0:
            assert hash_table.get(word) == word


def test_enormous_amount_of_info_prime(hash_table_prime):
    """Time to break the code."""
    for word in DICTIONARY:
        assert hash_table_prime.get(word) == word


def test_very_large_word_with_optimus_primus_hash(hash_table_prime):
    """Wow what a word."""
    hash_table_prime.set('abcdefghijklmnopqrstuvwxyz', 42)
    assert hash_table_prime.get('abcdefghijklmnopqrstuvwxyz') == 42


def test_change_val_of_item_in_table(hash_table_prime):
    """Change val of item in table."""
    hash_table_prime.set('apple', 42)
    assert hash_table_prime.get('apple') == 42
