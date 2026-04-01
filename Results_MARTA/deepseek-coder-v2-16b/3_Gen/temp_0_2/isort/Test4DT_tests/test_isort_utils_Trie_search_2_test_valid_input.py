
import pytest
from isort.utils import Trie, TrieNode
from pathlib import Path
from typing import Any

def test_valid_input():
    trie = Trie(config_file="initial_config.yaml", config_data={"key": "value"})
    
    # Test with a valid filename that exists in the trie structure
    result = trie.search("desired_file_path")
    assert isinstance(result, tuple)
    assert isinstance(result[1], dict)
    assert result == ("initial_config.yaml", {"key": "value"})

    # Test with a valid filename that does not exist in the trie structure but has a closest match
    result = trie.search("non_existent_file")
    assert isinstance(result, tuple)
    assert isinstance(result[1], dict)
    assert result == ("initial_config.yaml", {"key": "value"})

    # Test with an invalid filename that should return the default config
    result = trie.search("invalid/path/file")
    assert isinstance(result, tuple)
    assert isinstance(result[1], dict)
    assert result == ("initial_config.yaml", {"key": "value"})
