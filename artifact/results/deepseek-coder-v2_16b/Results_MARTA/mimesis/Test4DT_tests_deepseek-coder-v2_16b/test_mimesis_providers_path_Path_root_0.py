
import pytest
from mimesis.providers.path import Path
from pathlib import PureWindowsPath, PurePosixPath
import sys

def test_valid_input_specified_platform():
    path_instance = Path(platform='win32')
    assert path_instance.platform == 'win32'
    assert isinstance(path_instance._pathlib_home, PureWindowsPath)

def test_invalid_input_none_platform():
    with pytest.raises(TypeError):
        path_instance = Path(platform=None)
