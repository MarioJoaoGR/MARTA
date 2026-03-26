
import pytest
from isort.exceptions import FileSkipSetting

def test_invalid_input():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("example/file.py")
