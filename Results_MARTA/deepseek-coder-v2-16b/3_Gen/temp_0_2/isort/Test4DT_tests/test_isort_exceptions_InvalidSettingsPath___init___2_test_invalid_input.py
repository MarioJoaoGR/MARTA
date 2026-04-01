
import pytest
from isort.exceptions import InvalidSettingsPath

def test_invalid_input():
    with pytest.raises(InvalidSettingsPath):
        raise InvalidSettingsPath("non/existent/path")
