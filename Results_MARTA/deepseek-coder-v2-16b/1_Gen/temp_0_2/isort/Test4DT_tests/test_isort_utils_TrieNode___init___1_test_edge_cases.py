
import pytest
from typing import Any

class TrieNode:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        if not config_data:
            config_data = {}

        self.nodes: dict[str, TrieNode] = {}
        self.config_info: tuple[str, dict[str, Any]] = (config_file, config_data)

def test_edge_cases():
    # Test with None for config_file and empty dictionary for config_data
    node1 = TrieNode(config_file=None, config_data={})
    assert node1.config_info == (None, {})

    # Test with empty string for config_file and empty dictionary for config_data
    node2 = TrieNode(config_file="", config_data={})
    assert node2.config_info == ("", {})

    # Test with None for config_file and non-empty dictionary for config_data
    node3 = TrieNode(config_file=None, config_data={"key": "value"})
    assert node3.config_info == (None, {"key": "value"})

    # Test with empty string for config_file and non-empty dictionary for config_data
    node4 = TrieNode(config_file="", config_data={"key": "value"})
    assert node4.config_info == ("", {"key": "value"})
