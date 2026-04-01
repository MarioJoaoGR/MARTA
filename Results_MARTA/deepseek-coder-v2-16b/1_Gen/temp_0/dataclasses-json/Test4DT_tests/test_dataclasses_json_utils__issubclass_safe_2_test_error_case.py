
import pytest
from dataclasses_json.utils import _issubclass_safe

def test_error_case():
    class InvalidClass:
        pass
    
    # Test with invalid inputs that should not raise exceptions
    assert not _issubclass_safe(InvalidClass, int)
