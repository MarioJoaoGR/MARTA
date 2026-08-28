
import os
import json
import stat
from ansible.galaxy.api import _load_cache
import pytest

def test_nonexistent_file():
    nonexistent_path = '/new/path/to/your/cachefile'
    with pytest.raises(FileNotFoundError):
        _load_cache(nonexistent_path)

