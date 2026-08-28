
import pytest
from isort.exceptions import FileSkipSetting

def test_file_skip_setting_with_valid_string():
    file_path = "path/to/your_script.py"
    exception = FileSkipSetting(file_path)
    
    assert str(exception) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

