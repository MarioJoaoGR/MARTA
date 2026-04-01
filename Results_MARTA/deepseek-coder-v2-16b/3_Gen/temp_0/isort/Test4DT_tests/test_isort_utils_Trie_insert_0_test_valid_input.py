
from pathlib import Path

import pytest

from isort.utils import Trie, TrieNode


def test_valid_input():
    trie = Trie()
    config_file = "path/to/config"
    config_data = {"key": "value"}
    
    trie.insert(config_file, config_data)
    
    resolved_config_path_as_tuple = Path(config_file).parent.resolve().parts
    temp = trie.root
    
    for path in resolved_config_path_as_tuple:
        assert path in temp.nodes, f"Node {path} not found in the Trie."
        temp = temp.nodes[path]
    
    assert temp.config_info == (config_file, config_data), "Config info does not match the inserted data."
