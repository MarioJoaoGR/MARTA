
import pytest
from isort.utils import Trie, TrieNode
from pathlib import Path

def test_none_input():
    trie = Trie()
    result = trie.search("non_existent_file")
    assert result == ("", {})
