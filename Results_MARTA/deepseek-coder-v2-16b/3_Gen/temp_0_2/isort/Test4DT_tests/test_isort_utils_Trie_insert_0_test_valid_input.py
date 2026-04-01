
import pytest
from pathlib import Path
from typing import Any

class TrieNode:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.nodes: dict[str, TrieNode] = {}
        self.config_info: tuple[str, dict[str, Any]] | None = (config_file, config_data) if config_data else None

class Trie:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.root: TrieNode = TrieNode(config_file, config_data)

    def insert(self, config_file: str, config_data: dict[str, Any]) -> None:
        resolved_config_path_as_tuple = Path(config_file).parent.resolve().parts

        temp = self.root

        for path in resolved_config_path_as_tuple:
            if path not in temp.nodes:
                temp.nodes[path] = TrieNode()

            temp = temp.nodes[path]

        temp.config_info = (config_file, config_data)

@pytest.fixture
def valid_trie():
    return Trie()

def test_valid_input(valid_trie):
    config_file = "example/config/file"
    config_data = {"key": "value"}
    valid_trie.insert(config_file, config_data)
    
    current_node = valid_trie.root
    path_parts = Path(config_file).parent.resolve().parts
    
    for part in path_parts:
        assert part in current_node.nodes
        current_node = current_node.nodes[part]
    
    assert current_node.config_info == (config_file, config_data)
