
import pytest
from isort.exceptions import FileSkipSetting

def test_valid_input():
    with pytest.raises(FileSkipSetting) as excinfo:
        raise FileSkipSetting("example/file/path")
    assert str(excinfo.value) == "example/file/path was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
