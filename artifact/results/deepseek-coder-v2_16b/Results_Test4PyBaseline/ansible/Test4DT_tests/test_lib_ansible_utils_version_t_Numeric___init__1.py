
# Module: ansible.utils.version
# test_numeric.py
from ansible.utils.version import _Numeric

def test_numeric_initialization_with_float():
    num1 = _Numeric(5.0)
    assert isinstance(num1, _Numeric), "Initialization with a float should create an instance of _Numeric"