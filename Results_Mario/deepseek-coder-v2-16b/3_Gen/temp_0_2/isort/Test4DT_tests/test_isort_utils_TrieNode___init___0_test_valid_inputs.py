
import pytest
from typing import Any

class TrieNode:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        if not config_data:
            config_data = {}

        self.nodes: dict[str, TrieNode] = {}
        self.config_info: tuple[str, dict[str, Any]] = (config_file, config_data)

def test_valid_inputs():
    # Create an instance of TrieNode with valid config_file and config_data
    trie_node = TrieNode(config_file="path/to/config", config_data={"key": "value"})
    
    # Assert that the instance was created correctly
    assert isinstance(trie_node, TrieNode)
    assert trie_node.config_info == ("path/to/config", {"key": "value"})
    assert trie_node.nodes == {}
