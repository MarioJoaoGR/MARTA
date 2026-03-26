
import pytest
from unittest.mock import patch
from isort.settings import _get_config_data

@pytest.mark.parametrize("file_path, sections, expected", [
    ("path/to/tomlfile.toml", ("section1", "section2"), {"section1": {}, "section2": {}}),
    ("path/to/editorconfigfile", ("*.{ext}", "section3"), {"*.{ext}": {}, "section3": {}})
])
def test_get_config_data(file_path, sections, expected):
    with patch('builtins.open', mock_open()):
        config = _get_config_data(file_path, sections)
        assert config == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__get_config_data_0_test_edge_cases
isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_edge_cases.py:11:32: E0602: Undefined variable 'mock_open' (undefined-variable)


"""