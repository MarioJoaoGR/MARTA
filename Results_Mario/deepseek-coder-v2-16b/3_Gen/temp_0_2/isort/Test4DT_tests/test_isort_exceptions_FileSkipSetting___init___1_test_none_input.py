
import pytest
from isort.exceptions import FileSkipSetting

def test_none_input():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("example/file/path")
    
    assert str(exc_info.value) == "example/file/path was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
