
import pytest
from unittest.mock import patch
from isort.settings import _get_config_data

@pytest.mark.parametrize("file_path, sections, expected_output", [
    # Add your test cases here with file path and expected output
])
def test_invalid_inputs(file_path, sections, expected_output):
    with pytest.raises(Exception) as excinfo:
        _get_config_data(file_path, sections)
    assert str(excinfo.value) == expected_output
