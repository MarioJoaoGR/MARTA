
import pytest
from pathlib import Path, PureWindowsPath, PurePosixPath
from unittest.mock import patch
from mimesis.providers.path import Path

# Test for default platform initialization

# Test for invalid platform input error handling

# Test for specific platform initialization
@patch('sys.platform', 'linux')
def test_specific_platform_initialization():
    path_instance = Path(platform='linux')
    assert path_instance.platform == 'linux', f"Expected 'linux' but got {path_instance.platform}"