
import pytest
from httpie.models import OutputOptions

def test_any():
    # Test when all options are set to False
    options = OutputOptions(kind=None, headers=False, body=False, meta=False)
    assert not options.any(), "Expected any() to return False when no options are True"

    # Test when only headers is set to True
    options = OutputOptions(kind=None, headers=True, body=False, meta=False)
    assert options.any(), "Expected any() to return True when headers are True"

    # Test when only body is set to True
    options = OutputOptions(kind=None, headers=False, body=True, meta=False)
    assert options.any(), "Expected any() to return True when body is True"

    # Test when only meta is set to True
    options = OutputOptions(kind=None, headers=False, body=False, meta=True)
    assert options.any(), "Expected any() to return True when meta is True"

    # Test when all options are set to True
    options = OutputOptions(kind=None, headers=True, body=True, meta=True)
    assert options.any(), "Expected any() to return True when all options are True"
