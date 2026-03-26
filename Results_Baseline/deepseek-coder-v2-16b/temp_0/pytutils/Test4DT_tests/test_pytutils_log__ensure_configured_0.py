# Module: pytutils.log
import pytest
from pytutils.log import _ensure_configured, configure, _CONFIGURED

# Test that the function does not reconfigure if already configured
def test_already_configured():
    assert len(_CONFIGURED) == 0  # Ensure it starts unconfigured
    _ensure_configured()
    assert len(_CONFIGURED) == 1  # Ensure it gets configured after first call
    _ensure_configured()
    assert len(_CONFIGURED) == 1  # Ensure it remains configured on subsequent calls

# Test forcing configuration even if already configured in a testing scenario
def test_force_configure():
    _CONFIGURED.append(True)  # Simulate being already configured
    assert _CONFIGURED[-1] is True  # Verify the state before and after function call
    _ensure_configured([])
    assert len(_CONFIGURED) == 2  # Ensure it remains configured after force configuration
