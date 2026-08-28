
import pytest
from mimesis.providers.path import Path
from pathlib import PurePosixPath, PureWindowsPath
import sys

# Test initialization with valid platform 'darwin'

# Test initialization with invalid platform
def test_invalid_input():
    with pytest.raises(KeyError):
        Path(platform='unsupported_platform')