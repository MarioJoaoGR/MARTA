
import pytest

from isort.exceptions import InvalidSettingsPath


def test_edge_case_none():
    settings_path = None
    with pytest.raises(InvalidSettingsPath):
        raise InvalidSettingsPath(settings_path)
