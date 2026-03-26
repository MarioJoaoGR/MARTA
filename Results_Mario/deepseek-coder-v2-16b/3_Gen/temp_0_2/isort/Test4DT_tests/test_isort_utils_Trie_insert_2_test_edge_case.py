
import pytest
from pathlib import Path
from typing import Any

class TrieNode:
    def __init__(self, config_file="", config_data=None):
        self.nodes = {}
        self.config_info = (config_file, config_data) if config_data else None

class Trie:
    def __init__(self, config_file="", config_data=None):
        self.root = TrieNode(config_file, config_data)

    def insert(self, config_file: str, config_data: dict[str, Any]) -> None:
        resolved_config_path_as_tuple = Path(config_file).parent.resolve().parts

        temp = self.root

        for path in resolved_config_path_as_tuple:
            if path not in temp.nodes:
                temp.nodes[path] = TrieNode()

            temp = temp.nodes[path]

        temp.config_info = (config_file, config_data)

def test_edge_case():
    trie = Trie()
    with pytest.raises(TypeError):
        trie.insert(None, None)
