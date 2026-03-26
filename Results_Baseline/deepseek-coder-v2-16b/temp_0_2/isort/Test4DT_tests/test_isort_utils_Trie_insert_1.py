
from pathlib import Path
from typing import Any

import pytest

from isort.utils import (  # Replace with actual imports if they are not standard or defined elsewhere
    Trie, TrieNode)


# Test initialization of TrieNode with config_file
def test_trie_node_init_with_config_file():
    trie_node = TrieNode(config_file="path/to/config/file")
    assert isinstance(trie_node.nodes, dict)
    assert not trie_node.nodes
    assert trie_node.config_info == ("path/to/config/file", {})

# Test initialization of TrieNode with config_data
def test_trie_node_init_with_config_data():
    config_data = {"key1": "value1", "key2": "value2"}
    trie_node = TrieNode(config_data=config_data)
    assert isinstance(trie_node.nodes, dict)
    assert not trie_node.nodes