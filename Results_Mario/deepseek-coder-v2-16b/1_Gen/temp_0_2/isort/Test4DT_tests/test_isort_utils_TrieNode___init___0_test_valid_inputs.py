
import pytest
from isort.utils import TrieNode

def test_valid_inputs():
    # Test initializing a TrieNode without any config_file or config_data
    node = TrieNode()
    assert isinstance(node, TrieNode)
    assert node.nodes == {}
    assert node.config_info == ("", {})

    # Test initializing a TrieNode with a config_file
    node = TrieNode(config_file="path/to/config")
    assert isinstance(node, TrieNode)
    assert node.nodes == {}
    assert node.config_info == ("path/to/config", {})

    # Test initializing a TrieNode with config_data
    node = TrieNode(config_data={"key": "value"})
    assert isinstance(node, TrieNode)
    assert node.nodes == {}
    assert node.config_info == ("", {"key": "value"})
