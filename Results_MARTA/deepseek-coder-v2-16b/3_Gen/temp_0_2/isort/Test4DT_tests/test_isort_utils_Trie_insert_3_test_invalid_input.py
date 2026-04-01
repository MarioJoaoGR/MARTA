
import pytest
from isort.utils import Trie, TrieNode
from pathlib import Path

def test_invalid_input():
    trie = Trie()
    
    # Test inserting a non-string path
    with pytest.raises(TypeError):
        trie.insert(12345, {"key": "value"})
