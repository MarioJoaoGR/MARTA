
import os
import urllib.request
from typing import Optional
from unittest.mock import patch, MagicMock
import pytest
from flutes.network import _download

@pytest.mark.parametrize("url, filename, path, bar_fn", [
    (None, "example_file", ".", None),  # Invalid URL type
    ("http://example.com/file", None, ".", None),  # Invalid filename type
    ("http://example.com/file", "example_file", None, None),  # Invalid path type
])
def test_invalid_inputs(url, filename, path, bar_fn):
    with pytest.raises(TypeError):
        _download(url, filename, path, bar_fn)
