
import pytest
from isort.exceptions import FileSkipSetting

def test_invalid_input():
    file_path = 12345
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(file_path)
    
    assert str(exc_info.value) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
