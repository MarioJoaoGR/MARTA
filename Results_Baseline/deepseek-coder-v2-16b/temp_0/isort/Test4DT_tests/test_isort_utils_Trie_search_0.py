
# Module: isort.utils
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