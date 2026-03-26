
from pathlib import Path

import pytest

from isort.utils import Trie, TrieNode


# Test initialization without arguments
def test_trie_init_without_args():
    trie = Trie()
    assert isinstance(trie.root, TrieNode)
    assert trie.root.config_info == ("", {})

# Test initialization with configuration file and data
def test_trie_init_with_config_file_and_data():
    trie = Trie(config_file="path/to/config", config_data={"key": "value"})
    assert isinstance(trie.root, TrieNode)
    assert trie.root.config_info == ("path/to/config", {"key": "value"})

# Test inserting a new configuration into the Trie
def test_insert_new_configuration():
    trie = Trie()
    trie.insert("new_config_file.yaml", {"key": "value"})
    assert isinstance(trie.root, TrieNode)

# Test search function with a simple path that matches the config file
def test_search_simple_path():
    trie = Trie()
    trie.insert("config_file.yaml", {"key": "value"})
    filename = "some/directory/structure/config_file.yaml"
    assert trie.search(filename) == ("config_file.yaml", {"key": "value"})

# Test search function with a path that does not match any config file
def test_search_no_match():
    trie = Trie()
    filename = "some/directory/structure/nofile.yaml"
    assert trie.search(filename) == ("", {})

# Test search function with an empty path
def test_search_empty_path():
    trie = Trie()
    filename = ""
    assert trie.search(filename) == ("", {})

# Test search function with a None path
def test_search_none_path():
    trie = Trie()
    filename = None