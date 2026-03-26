
import pytest
from unittest.mock import patch, MagicMock
from flutes.network import download
import os
import tempfile
import tarfile
import zipfile

@pytest.mark.parametrize("url, save_dir, filename, extract, progress, bar_fn, expected", [
    # Test invalid input cases here
])
def test_invalid_input(url, save_dir, filename, extract, progress, bar_fn, expected):
    with pytest.raises(expected):
        download(url, save_dir, filename, extract, progress, bar_fn)
