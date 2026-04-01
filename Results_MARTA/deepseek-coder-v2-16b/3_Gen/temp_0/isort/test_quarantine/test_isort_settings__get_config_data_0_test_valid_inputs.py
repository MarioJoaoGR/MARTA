
import pytest
from unittest.mock import patch, mock_open
import tomllib
import configparser
import os
from isort.settings import _get_config_data

@pytest.mark.parametrize("file_path, sections, expected", [
    ("path/to/tomlfile.toml", ("section1", "section2"), {"section1": {}, "section2": {}}),
    ("path/to/editorconfigfile", ("*.{ext}", "section3"), {"*.{ext}": {}, "section3": {}})
])
def test_get_config_data(file_path, sections, expected):
    with patch("builtins.open", mock_open()) as mock_file:
        if file_path.endswith(".toml"):
            mock_file.return_value.__enter__.return_value = tomllib.dumps({"section1": {}, "section2": {}}).encode()
        elif file_path.endswith(".editorconfig"):
            mock_file.return_value.__enter__.return_value = "\n".join([
                "[section1]",
                "key1=value1",
                "[section2]",
                "key2=value2"
            ])
        assert _get_config_data(file_path, sections) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__get_config_data_0_test_valid_inputs
isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_inputs.py:16:60: E1101: Module 'tomllib' has no 'dumps' member (no-member)


"""