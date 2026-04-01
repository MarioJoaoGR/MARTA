
import pytest
from isort.exceptions import FileSkipSetting

def test_edge_case_none():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("example/file.py")
