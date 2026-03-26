
import os
from isort.exceptions import InvalidSettingsPath
from unittest.mock import patch
import pytest

def test_invalid_input():
    invalid_path = 'non_existent_file.cfg'
    with pytest.raises(InvalidSettingsPath):
        raise InvalidSettingsPath(invalid_path)
