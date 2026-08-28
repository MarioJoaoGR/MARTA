
import pytest
from pathlib import Path, PosixPath, WindowsPath
import os
from flutils.pathutils import normalize_path


def test_valid_case_byte_string():
    with pytest.raises(AttributeError):
        normalize_path(b'~/tmp/foo/../bar'.encode('utf-8'))
