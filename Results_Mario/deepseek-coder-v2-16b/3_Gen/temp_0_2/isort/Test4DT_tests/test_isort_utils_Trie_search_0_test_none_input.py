
import pytest
from pathlib import Path
from typing import Any

class TrieNode:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.config_info = (config_file, config_data if config_data is not None else {})
        self.nodes: dict[str, TrieNode] = {}

class Trie:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.root: TrieNode = TrieNode(config_file, config_data)

    def search(self, filename: str) -> tuple[str, dict[str, Any]]:
        resolved_file_path_as_tuple = Path(filename).resolve().parts
        temp = self.root
        last_stored_config: tuple[str, dict[str, Any]] = ("", {})
        for path in resolved_file_path_as_tuple:
            if temp.config_info[0]:
                last_stored_config = temp.config_info
            if path not in temp.nodes:
                break
            temp = temp.nodes[path]
        return last_stored_config

def test_none_input():
    trie = Trie()
    result = trie.search("some_file")
    assert result == ("", {})
