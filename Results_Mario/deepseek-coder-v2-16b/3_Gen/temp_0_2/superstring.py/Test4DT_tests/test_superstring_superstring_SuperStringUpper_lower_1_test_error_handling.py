
import pytest
from superstring.superstring import SuperStringUpper

def test_error_handling():
    # Test setup
    s = SuperStringUpper(12345)
    
    # Test the lower method with a non-string type
    with pytest.raises(AttributeError):
        result = s.lower()
