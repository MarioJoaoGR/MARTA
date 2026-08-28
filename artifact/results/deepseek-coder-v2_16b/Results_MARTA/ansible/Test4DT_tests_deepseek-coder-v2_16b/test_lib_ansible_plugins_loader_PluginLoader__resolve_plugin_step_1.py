
import pytest
from ansible.plugins.loader import PluginLoader


def test_error_case():
    with pytest.raises(ValueError):
        raise ValueError("This is a test error case")