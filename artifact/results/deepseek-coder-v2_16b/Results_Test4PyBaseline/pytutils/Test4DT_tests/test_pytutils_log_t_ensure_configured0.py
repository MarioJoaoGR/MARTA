
import pytest
from pytutils.log import _ensure_configured, _CONFIGURED, configure
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

@pytest.fixture(autouse=True)
def reset_configuration():
    if hasattr(_CONFIGURED, 'append'):
        while len(_CONFIGURED):
            _CONFIGURED.pop()
    yield
    if hasattr(_CONFIGURED, 'append'):
        _CONFIGURED.append(False)  # Reset to default state for other tests

def test_ensure_configured_default():
    assert not _CONFIGURED
    _ensure_configured()
    assert _CONFIGURED == [True]

def test_ensure_configured_already_configured():
    _CONFIGURED.append(True)
    _ensure_configured()
    assert _CONFIGURED == [True]

def test_ensure_configured_with_custom_configuration():
    custom_config = []
    with patch('pytutils.log._CONFIGURED', custom_config):
        _ensure_configured()