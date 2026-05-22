
import json
from pathlib import Path
from typing import Dict, Any
from httpie.config import ConfigFileError
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("config_type, path", [('settings', Path('nonexistent.json'))])
def test_invalid_file(config_type: str, path: Path):
    with pytest.raises(ConfigFileError) as excinfo:
        read_raw_config(config_type, path)
    assert f'cannot read {config_type} file:' in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_config_read_raw_config_0_test_invalid_file
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_read_raw_config_0_test_invalid_file.py:12:8: E0602: Undefined variable 'read_raw_config' (undefined-variable)


"""