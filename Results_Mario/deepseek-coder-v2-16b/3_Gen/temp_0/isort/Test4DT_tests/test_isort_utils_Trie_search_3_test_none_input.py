
from pathlib import Path

import pytest

from isort.utils import Trie, TrieNode


def test_none_input():
    trie = Trie()
    result = trie.search("non_existent_file")
    assert result == ("", {})
