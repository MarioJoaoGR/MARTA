
import pytest
from isort.exceptions import InvalidSettingsPath

def test_edge_case_none():
    with pytest.raises(InvalidSettingsPath):
        raise InvalidSettingsPath(None)
