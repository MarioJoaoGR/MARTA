
from pathlib import Path
from typing import Any

import pytest

from isort.utils import Trie


# Test cases for the insert method of the Trie class
def test_insert_without_configuration():
    trie = Trie()
    config_file = "config_file"
    config_data = {"key": "value"}
    trie.insert(config_file, config_data)
    assert len(trie.root.nodes) == 1