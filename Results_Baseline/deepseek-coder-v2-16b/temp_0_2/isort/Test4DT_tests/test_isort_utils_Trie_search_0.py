
# Module: isort.utils
from pathlib import Path

import pytest

from isort.utils import Trie


# Test initialization with config file
def test_trie_init_with_config_file():
    trie = Trie(config_file="path/to/config/file")
    assert isinstance(trie, Trie)
    assert trie.root is not None

# Test initialization with config data dictionary
def test_trie_init_with_config_data():
    config_data = {"key1": "value1", "key2": "value2"}
    trie = Trie(config_data=config_data)
    assert isinstance(trie, Trie)
    assert trie.root is not None

# Test initialization without parameters (defaults to empty config data)
def test_trie_init_without_parameters():
    trie = Trie()
    assert isinstance(trie, Trie)
    assert trie.root is not None