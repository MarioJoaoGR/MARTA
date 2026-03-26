
import pytest

from isort.exceptions import FileSkipSetting


# Test cases for FileSkipSetting class
def test_basic_usage():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("example/file/path.py")
    assert str(exc_info.value) == "example/file/path.py was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

def test_custom_message():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting("example/file/path.py", custom_message="Custom reason for skipping")