
import pytest
from isort.exceptions import FileSkipSetting

def test_invalid_input():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(12345)  # Providing an invalid input type (non-string)
    
    assert str(exc_info.value) == "12345 was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
