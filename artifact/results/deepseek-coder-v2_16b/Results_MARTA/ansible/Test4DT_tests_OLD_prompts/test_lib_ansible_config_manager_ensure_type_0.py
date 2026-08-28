
import pytest
from ansible.config.manager import ensure_type

def test_valid_inputs():
    assert ensure_type(123, 'integer') == 123
    assert ensure_type('True', 'boolean') is True

