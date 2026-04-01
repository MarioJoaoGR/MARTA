
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import os
import tempfile
import tarfile
import zipfile
from flutes.network import download

@pytest.mark.parametrize("url, save_dir, filename, extract, progress, bar_fn", [
    (None, None, None, False, False, None),  # Test with all None values
])
def test_edge_case_none_values(url, save_dir, filename, extract, progress, bar_fn):
    with pytest.raises(TypeError):
        download(url, save_dir, filename, extract, progress, bar_fn)
