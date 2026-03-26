
import pytest
from pathlib import Path
from unittest.mock import patch
from isort.utils import Trie, TrieNode

def test_nonexistent_file():
    trie = Trie()
    with patch('isort.utils.TrieNode.__init__', return_value=None):
        result = trie.search("non_existent_file")
        assert result == ("", {})
