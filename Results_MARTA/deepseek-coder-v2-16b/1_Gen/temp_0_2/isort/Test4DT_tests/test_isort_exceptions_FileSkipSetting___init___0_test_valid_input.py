
import pytest
from isort.exceptions import FileSkipSetting

def test_valid_input():
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting('example/file.py')
    
    assert str(exc_info.value) == "example/file.py was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
